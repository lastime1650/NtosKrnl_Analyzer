# HalAllocateCommonBufferWithBoundsDmarThin

- RVA: `0x00552BF0`–`0x00552C61` (길이 `113` bytes)
- VA: `0x0000000140552BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3E08`
- 디코드: `29`개 명령, `113/113` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00552C3F` → [HalpAllocateCommonBufferDmarThin](../3E/HalpAllocateCommonBufferDmarThin_function_003E8FF0.md) (function, `0x003E8FF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00552BF0  4C 8B DC                        mov r11, rsp
00552BF3  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
00552BF7  57                              push rdi
00552BF8  48 83 EC 50                     sub rsp, 0x50
00552BFC  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
00552C04  49 8D 43 08                     lea rax, [r11 + 8]
00552C08  48 8B 89 00 02 00 00            mov rcx, qword ptr [rcx + 0x200]
00552C0F  33 DB                           xor ebx, ebx
00552C11  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00552C15  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00552C1C  49 89 7B E0                     mov qword ptr [r11 - 0x20], rdi
00552C20  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00552C24  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00552C2C  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
00552C30  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00552C37  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00552C3B  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00552C3F  E8 AC 63 E9 FF                  call 0x1403e8ff0
00552C44  85 C0                           test eax, eax
00552C46  79 05                           jns 0x140552c4d
00552C48  48 89 1F                        mov qword ptr [rdi], rbx
00552C4B  EB 05                           jmp 0x140552c52
00552C4D  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00552C52  48 8B C3                        mov rax, rbx
00552C55  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00552C5A  48 83 C4 50                     add rsp, 0x50
00552C5E  5F                              pop rdi
00552C5F  C3                              ret
00552C60  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalAllocateCommonBufferWithBoundsDmarThin(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    v_rsp = (v_rsp) - (80);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 8;
    *(unsigned __int64 *)(v_rsp - 32) = a8;
    v_stack_m28 = (unsigned int)((unsigned int)(a7));
    *(unsigned __int64 *)(v_rsp - 48) = a6;
    v_stack_m38 = (unsigned int)((unsigned int)(a5));
    *(unsigned __int64 *)(v_rsp + 8) = 0;
    result = HalpAllocateCommonBufferDmarThin(*(unsigned __int64 *)(a1 + 512), a2, a3, a4);
    if (!sign_flag) goto loc_00552C4D;
    *(unsigned __int64 *)(a8) = 0;
    goto loc_00552C52;
loc_00552C4D:
loc_00552C52:
    v_rsp = (v_rsp) + (80);
    return v_stack_p8;
}
```

## 5. (Beta) C Style

```c
int64_t HalAllocateCommonBufferWithBoundsDmarThin(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    local_rsp = (local_rsp) - (80);
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 8;
    *(void **)(local_rsp - 0x20) = Arg8;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg7));
    *(uint64_t *)(local_rsp - 0x30) = Arg6;
    v_stack_m38 = (uint32_t)((uint32_t)(Arg5));
    *(uint64_t *)(local_rsp + 0x8) = 0;
    result = HalpAllocateCommonBufferDmarThin(*(uint64_t *)(arg1 + 0x200), Arg2, Arg3, Arg4);
    if (!sign_flag) goto loc_00552C4D;
    *(uint64_t *)(arg8) = 0;
    goto loc_00552C52;
loc_00552C4D:
loc_00552C52:
    local_rsp = (local_rsp) + (80);
    return v_stack_p8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x200` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00552BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00552BF0[BB_00552BF0]
  bb_00552C48[BB_00552C48]
  bb_00552C4D[BB_00552C4D]
  bb_00552C52[BB_00552C52]
  bb_00552C60[BB_00552C60]
  bb_00552BF0 -->|branch| bb_00552C4D
  bb_00552BF0 -->|fallthrough| bb_00552C48
  bb_00552C48 -->|branch| bb_00552C52
  bb_00552C4D -->|flow| bb_00552C52
```
