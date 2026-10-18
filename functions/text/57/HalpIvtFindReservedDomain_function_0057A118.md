# HalpIvtFindReservedDomain

- RVA: `0x0057A118`–`0x0057A166` (길이 `78` bytes)
- VA: `0x000000014057A118`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071750`
- 디코드: `25`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IvtGetBlockedDomain](../4D/IvtGetBlockedDomain_function_004D2204.md) at `0x004D221B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057A118  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0057A11D  4C 8B 91 60 01 00 00            mov r10, qword ptr [rcx + 0x160]
0057A124  45 33 C9                        xor r9d, r9d
0057A127  8B DA                           mov ebx, edx
0057A129  45 8B C1                        mov r8d, r9d
0057A12C  45 8B 1A                        mov r11d, dword ptr [r10]
0057A12F  45 3B C3                        cmp r8d, r11d
0057A132  73 28                           jae 0x14057a15c
0057A134  41 8B C8                        mov ecx, r8d
0057A137  48 03 C9                        add rcx, rcx
0057A13A  49 8B 44 CA 10                  mov rax, qword ptr [r10 + rcx*8 + 0x10]
0057A13F  48 8B 10                        mov rdx, qword ptr [rax]
0057A142  83 3A 01                        cmp dword ptr [rdx], 1
0057A145  75 08                           jne 0x14057a14f
0057A147  0F B7 42 0C                     movzx eax, word ptr [rdx + 0xc]
0057A14B  3B C3                           cmp eax, ebx
0057A14D  74 05                           je 0x14057a154
0057A14F  41 FF C0                        inc r8d
0057A152  EB DB                           jmp 0x14057a12f
0057A154  4D 8D 4A 08                     lea r9, [r10 + 8]
0057A158  4D 8D 0C C9                     lea r9, [r9 + rcx*8]
0057A15C  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
0057A161  49 8B C1                        mov rax, r9
0057A164  C3                              ret
0057A165  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIvtFindReservedDomain(__int64 a1, int a2, __int64 a3, int a4)
{
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    a4 = 0;
loc_0057A12F:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352)))))) goto loc_0057A15C;
    a1 = (0) + (0);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352) + a1 * 8 + 16)))) != 1) goto loc_0057A14F;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352) + a1 * 8 + 16)) + 12))) == ((unsigned int)((unsigned int)(a2)))) goto loc_0057A154;
loc_0057A14F:
    a3 = (unsigned int)((0) + 1);
    goto loc_0057A12F;
loc_0057A154:
loc_0057A15C:
    return *(unsigned __int64 *)(a1 + 352) + 8 + a1 * 8;
}
```

## 5. (Beta) C Style

```c
int64_t HalpIvtFindReservedDomain(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    Arg4 = 0;
loc_0057A12F:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160)))))) goto loc_0057A15C;
    Arg1 = (0) + (0);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160) + arg1 * 8 + 0x10)))) != 1) goto loc_0057A14F;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160) + arg1 * 8 + 0x10)) + 0xC))) == ((uint32_t)((uint32_t)(Arg2)))) goto loc_0057A154;
loc_0057A14F:
    Arg3 = (uint32_t)((0) + 1);
    goto loc_0057A12F;
loc_0057A154:
loc_0057A15C:
    return *(uint64_t *)(arg1 + 0x160) + 8 + Arg1 * 8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x160` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057A118&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057A118[BB_0057A118]
  bb_0057A12F[BB_0057A12F]
  bb_0057A134[BB_0057A134]
  bb_0057A147[BB_0057A147]
  bb_0057A14F[BB_0057A14F]
  bb_0057A154[BB_0057A154]
  bb_0057A15C[BB_0057A15C]
  bb_0057A165[BB_0057A165]
  bb_0057A118 -->|flow| bb_0057A12F
  bb_0057A12F -->|branch| bb_0057A15C
  bb_0057A12F -->|fallthrough| bb_0057A134
  bb_0057A134 -->|branch| bb_0057A14F
  bb_0057A134 -->|fallthrough| bb_0057A147
  bb_0057A147 -->|branch| bb_0057A154
  bb_0057A147 -->|fallthrough| bb_0057A14F
  bb_0057A14F -->|branch| bb_0057A12F
  bb_0057A154 -->|flow| bb_0057A15C
```
