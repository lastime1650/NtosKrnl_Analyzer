# sub_0037BF15

- RVA: `0x0037BF15`–`0x0037BFA1` (길이 `140` bytes)
- VA: `0x000000014037BF15`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B1AC`
- 디코드: `28`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0037BF3D` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x0037BF4B` → RVA `0x00FC53E0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0037BF22` → [sub_0037B54F + 0x30B](Unknown_function_0037B54F.md) (`tail-transfer`)
  - `0x0037BF5F` → [sub_0037B54F + 0x30B](Unknown_function_0037B54F.md) (`tail-transfer`)
  - `0x0037BF8F` → [sub_0037B54F + 0x355](Unknown_function_0037B54F.md) (`tail-transfer`)
  - `0x0037BF9C` → [sub_0037B54F + 0x355](Unknown_function_0037B54F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0037BF15  41 0F B6 86 04 02 00 00         movzx eax, byte ptr [r14 + 0x204]
0037BF1D  8B D0                           mov edx, eax
0037BF1F  83 F8 07                        cmp eax, 7
0037BF22  0F 83 32 F9 FF FF               jae 0x14037b85a
0037BF28  41 8B 46 54                     mov eax, dword ptr [r14 + 0x54]
0037BF2C  41 8B 4E 50                     mov ecx, dword ptr [r14 + 0x50]
0037BF30  3B C8                           cmp ecx, eax
0037BF32  0F 46 C8                        cmovbe ecx, eax
0037BF35  41 0F B6 86 05 02 00 00         movzx eax, byte ptr [r14 + 0x205]
0037BF3D  3B 0D 39 94 C4 00               cmp ecx, dword ptr [rip + 0xc49439]
0037BF43  41 0F 93 C7                     setae r15b
0037BF47  41 8D 0C 57                     lea ecx, [r15 + rdx*2]
0037BF4B  0F AF 0D 8E 94 C4 00            imul ecx, dword ptr [rip + 0xc4948e]
0037BF52  03 C8                           add ecx, eax
0037BF54  48 8B 86 B0 86 00 00            mov rax, qword ptr [rsi + 0x86b0]
0037BF5B  48 01 3C C8                     add qword ptr [rax + rcx*8], rdi
0037BF5F  E9 F6 F8 FF FF                  jmp 0x14037b85a
0037BF64  4C 8B 86 C0 00 00 00            mov r8, qword ptr [rsi + 0xc0]
0037BF6B  49 8B 86 40 02 00 00            mov rax, qword ptr [r14 + 0x240]
0037BF72  41 0F B7 88 88 00 00 00         movzx ecx, word ptr [r8 + 0x88]
0037BF7A  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
0037BF7F  49 8B 88 80 00 00 00            mov rcx, qword ptr [r8 + 0x80]
0037BF86  48 8B C1                        mov rax, rcx
0037BF89  48 23 C2                        and rax, rdx
0037BF8C  48 3B C1                        cmp rax, rcx
0037BF8F  0F 84 0F F9 FF FF               je 0x14037b8a4
0037BF95  48 01 BE A8 86 00 00            add qword ptr [rsi + 0x86a8], rdi
0037BF9C  E9 03 F9 FF FF                  jmp 0x14037b8a4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0037BF15(void)
{
    __int64 v_r15;

    a1 = (unsigned int)(*(unsigned int *)(v_r14 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 84))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 84))); }
    v_r15 = (((unsigned int)(a1)) >= (*(unsigned int *)(v_rip + 12883001))) ? 1 : 0;
    a1 = (unsigned int)((v_r15 + (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r14 + 516))) * 2) * (*(unsigned int *)(v_rip + 12883086)));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int8 *)(v_r14 + 517))));
}
```

## 5. (Beta) C Style

```c
void sub_0037BF15(void)
{
    int64_t local_r15;

    a1 = (uint32_t)(*(uint32_t *)(local_r14 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x54))))) { a1 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x54))); }
    local_r15 = (((uint32_t)(a1)) >= (*(uint32_t *)(v_rip + 0xC49439))) ? 1 : 0;
    a1 = (uint32_t)((local_r15 + (uint32_t)((uint32_t)(*(uint8_t *)(local_r14 + 0x204))) * 2) * (*(uint32_t *)(v_rip + 0xC4948E)));
    a1 = (uint32_t)((a1) + ((uint32_t)(*(uint8_t *)(local_r14 + 0x205))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037BF15&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0037BF15[BB_0037BF15]
  bb_0037BF28[BB_0037BF28]
  bb_0037BF64[BB_0037BF64]
  bb_0037BF95[BB_0037BF95]
  bb_0037BF15 -->|fallthrough| bb_0037BF28
  bb_0037BF64 -->|fallthrough| bb_0037BF95
```
