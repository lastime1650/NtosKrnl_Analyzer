# HalpHpetArmTimer

- RVA: `0x004AC5C0`–`0x004AC604` (길이 `68` bytes)
- VA: `0x00000001404AC5C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E680`
- 디코드: `19`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004AC5D5` → [HalSetTimerProblem](../4F/HalSetTimerProblem_function_004FC9A0.md) (function, `0x004FC9A0`)
- `0x004AC5FD` → [HalpHpetSetMatchValue](HalpHpetSetMatchValue_function_004AC60C.md) (function, `0x004AC60C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004AC5E8` → RVA `0x00F8FBB0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AC5C0  48 83 EC 28                     sub rsp, 0x28
004AC5C4  B8 00 00 00 80                  mov eax, 0x80000000
004AC5C9  4C 3B C0                        cmp r8, rax
004AC5CC  72 17                           jb 0x1404ac5e5
004AC5CE  45 33 C0                        xor r8d, r8d
004AC5D1  41 8D 50 04                     lea edx, [r8 + 4]
004AC5D5  E8 C6 03 05 00                  call 0x1404fc9a0
004AC5DA  B8 0D 00 00 C0                  mov eax, 0xc000000d
004AC5DF  48 83 C4 28                     add rsp, 0x28
004AC5E3  C3                              ret
004AC5E4  CC                              int3
004AC5E5  89 51 08                        mov dword ptr [rcx + 8], edx
004AC5E8  48 8B 15 C1 35 AE 00            mov rdx, qword ptr [rip + 0xae35c1]
004AC5EF  44 89 41 10                     mov dword ptr [rcx + 0x10], r8d
004AC5F3  90                              nop
004AC5F4  45 33 C0                        xor r8d, r8d
004AC5F7  8B 92 F0 00 00 00               mov edx, dword ptr [rdx + 0xf0]
004AC5FD  E8 0A 00 00 00                  call 0x1404ac60c
004AC602  EB DB                           jmp 0x1404ac5df
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpHpetArmTimer(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 < ((unsigned int)(0x80000000ULL))) goto loc_004AC5E5;
    a3 = 0;
    result = HalSetTimerProblem(a1, a3 + 4, a3, a4);
loc_004AC5DF:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC000000DULL);
loc_004AC5E5:
    *(unsigned int *)(a1 + 8) = (unsigned int)(a3 + 4);
    *(unsigned int *)(a1 + 16) = 0;
    a3 = 0;
    result = HalpHpetSetMatchValue(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11417025) + 240)), a3, a4);
    goto loc_004AC5DF;
}
```

## 5. (Beta) C Style

```c
int64_t HalpHpetArmTimer(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 < ((uint32_t)(0x80000000ULL))) goto loc_004AC5E5;
    Arg3 = 0;
    result = HalSetTimerProblem(Arg1, Arg3 + 4, Arg3, a4);
loc_004AC5DF:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC000000DULL);
loc_004AC5E5:
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(Arg3 + 4);
    *(uint32_t *)(arg1 + 0x10) = 0;
    Arg3 = 0;
    result = HalpHpetSetMatchValue(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAE35C1) + 0xF0)), Arg3, a4);
    goto loc_004AC5DF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x10` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AC5C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AC5C0[BB_004AC5C0]
  bb_004AC5CE[BB_004AC5CE]
  bb_004AC5DF[BB_004AC5DF]
  bb_004AC5E4[BB_004AC5E4]
  bb_004AC5E5[BB_004AC5E5]
  bb_004AC5C0 -->|branch| bb_004AC5E5
  bb_004AC5C0 -->|fallthrough| bb_004AC5CE
  bb_004AC5CE -->|flow| bb_004AC5DF
  bb_004AC5E4 -->|flow| bb_004AC5E5
  bb_004AC5E5 -->|branch| bb_004AC5DF
```
