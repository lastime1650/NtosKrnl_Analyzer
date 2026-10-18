# HalpTimerBuildKnownResourceIdString

- RVA: `0x00548A10`–`0x00548A5A` (길이 `74` bytes)
- VA: `0x0000000140548A10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2A4`
- 디코드: `17`개 명령, `74/74` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00548A4F` → [HalpExtBuildResourceIdString](HalpExtBuildResourceIdString_function_0054E494.md) (function, `0x0054E494`)

### Direct callers
- [HalpInitializeTimers](../53/HalpInitializeTimers_function_0053C1E0.md) at `0x0053C2E3`
- [HalpTimerRegister](../56/HalpTimerRegister_function_005616BC.md) at `0x005617CD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00548A10  48 83 EC 58                     sub rsp, 0x58
00548A14  44 0F B7 89 88 00 00 00         movzx r9d, word ptr [rcx + 0x88]
00548A1C  49 8B C0                        mov rax, r8
00548A1F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00548A24  45 33 D2                        xor r10d, r10d
00548A27  8B 81 8C 00 00 00               mov eax, dword ptr [rcx + 0x8c]
00548A2D  41 B8 00 41 00 00               mov r8d, 0x4100
00548A33  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00548A37  B9 4D 53 46 54                  mov ecx, 0x5446534d
00548A3C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00548A40  33 D2                           xor edx, edx
00548A42  66 44 89 54 24 28               mov word ptr [rsp + 0x28], r10w
00548A48  66 C7 44 24 20 01 00            mov word ptr [rsp + 0x20], 1
00548A4F  E8 40 5A 00 00                  call 0x14054e494
00548A54  48 83 C4 58                     add rsp, 0x58
00548A58  C3                              ret
00548A59  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerBuildKnownResourceIdString(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int16 v_stack_m30;
    unsigned __int16 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    v_stack_m18 = a3;
    v_r10 = 0;
    v_stack_m20 = a2;
    v_stack_m28 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 140)));
    a2 = 0;
    v_stack_m30 = 0;
    v_stack_m38 = 1;
    result = HalpExtBuildResourceIdString((unsigned int)(0x5446534DULL), a2, (unsigned int)(0x4100ULL), *(unsigned __int16 *)(a1 + 136));
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpTimerBuildKnownResourceIdString(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint16_t v_stack_m30;
    uint16_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    v_stack_m18 = Arg3;
    local_r10 = 0;
    v_stack_m20 = Arg2;
    v_stack_m28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8C)));
    Arg2 = 0;
    v_stack_m30 = 0;
    v_stack_m38 = 1;
    result = HalpExtBuildResourceIdString((uint32_t)(0x5446534DULL), Arg2, (uint32_t)(0x4100ULL), *(uint16_t *)(arg1 + 0x88));
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x88` | `16` | `R` |
| `Arg1` | `+ 0x8C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00548A10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00548A10[BB_00548A10]
  bb_00548A59[BB_00548A59]
```
