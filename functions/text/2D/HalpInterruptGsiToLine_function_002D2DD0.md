# HalpInterruptGsiToLine

- RVA: `0x002D2DD0`–`0x002D2E16` (길이 `70` bytes)
- VA: `0x00000001402D2DD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `25`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002D2DE2` → [HalpInterruptFindLinesForGsiRange](HalpInterruptFindLinesForGsiRange_function_002D204C.md) (function, `0x002D204C`)

### Direct callers
- [HalpTimerEnableHypervisorTimer](../4D/HalpTimerEnableHypervisorTimer_function_004D6ECC.md) at `0x004D6F6F`
- [HalpInterruptConnect](../54/HalpInterruptConnect_function_005426F8.md) at `0x005427B3`
- [HalpInterruptRemap](../54/HalpInterruptRemap_function_00542AE4.md) at `0x00542D64`
- [HalpInterruptSetLineSpecificOverride](../54/HalpInterruptSetLineSpecificOverride_function_0054468C.md) at `0x005446A1`
- [HalpTimerConfigureInterrupt](../54/HalpTimerConfigureInterrupt_function_00548AB0.md) at `0x00548CE3`
- [HalpTimerUnmapInterrupt](../54/HalpTimerUnmapInterrupt_function_0054A140.md) at `0x0054A1DC`
- [HalpTimerInitializeHypervisorTimer](../54/HalpTimerInitializeHypervisorTimer_function_0054B8F4.md) at `0x0054BA33`
- [HalpInterruptParseMadt](../55/HalpInterruptParseMadt_function_00557E74.md) at `0x005582EA`
- [sub_006DD9A0](../6D/Unknown_function_006DD9A0.md) at `0x006DD9E0`
- [sub_006FA83C](../6F/Unknown_function_006FA83C.md) at `0x006FA917`
- [HalpInterruptIsGsiValid](../../page/70/HalpInterruptIsGsiValid_function_007072F0.md) at `0x007072F9`
- [HalpInterruptUnmap](../../page/70/HalpInterruptUnmap_function_00707408.md) at `0x0070750F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002D2DD0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002D2DD5  57                              push rdi
002D2DD6  48 83 EC 20                     sub rsp, 0x20
002D2DDA  48 8B FA                        mov rdi, rdx
002D2DDD  8B D9                           mov ebx, ecx
002D2DDF  8D 51 01                        lea edx, [rcx + 1]
002D2DE2  E8 65 F2 FF FF                  call 0x1402d204c
002D2DE7  48 8B C8                        mov rcx, rax
002D2DEA  48 85 C0                        test rax, rax
002D2DED  74 20                           je 0x1402d2e0f
002D2DEF  8B 40 10                        mov eax, dword ptr [rax + 0x10]
002D2DF2  89 07                           mov dword ptr [rdi], eax
002D2DF4  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
002D2DF7  8B 49 14                        mov ecx, dword ptr [rcx + 0x14]
002D2DFA  2B C8                           sub ecx, eax
002D2DFC  03 CB                           add ecx, ebx
002D2DFE  89 4F 04                        mov dword ptr [rdi + 4], ecx
002D2E01  33 C0                           xor eax, eax
002D2E03  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002D2E08  48 83 C4 20                     add rsp, 0x20
002D2E0C  5F                              pop rdi
002D2E0D  C3                              ret
002D2E0E  CC                              int3
002D2E0F  B8 25 02 00 C0                  mov eax, 0xc0000225
002D2E14  EB ED                           jmp 0x1402d2e03
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInterruptGsiToLine(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = HalpInterruptFindLinesForGsiRange(a1, a1 + 1, a3, a4);
    if (result == 0) goto loc_002D2E0F;
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 20))) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + 28)))));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)((unsigned int)(a1)))));
    *(unsigned int *)(a2 + 4) = (unsigned int)(a1);
    result = 0;
loc_002D2E03:
    v_rsp = (v_rsp) + (32);
    return result;
loc_002D2E0F:
    goto loc_002D2E03;
}
```

## 5. (Beta) C Style

```c
int64_t HalpInterruptGsiToLine(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = HalpInterruptFindLinesForGsiRange(Arg1, Arg1 + 1, a3, a4);
    if (result == 0) goto loc_002D2E0F;
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x14))) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C)))));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
    *(uint32_t *)(arg2 + 0x4) = (uint32_t)(Arg1);
    result = 0;
loc_002D2E03:
    local_rsp = (local_rsp) + (32);
    return result;
loc_002D2E0F:
    goto loc_002D2E03;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x4` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D2DD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D2DD0[BB_002D2DD0]
  bb_002D2DEF[BB_002D2DEF]
  bb_002D2E03[BB_002D2E03]
  bb_002D2E0E[BB_002D2E0E]
  bb_002D2E0F[BB_002D2E0F]
  bb_002D2DD0 -->|branch| bb_002D2E0F
  bb_002D2DD0 -->|fallthrough| bb_002D2DEF
  bb_002D2DEF -->|flow| bb_002D2E03
  bb_002D2E0E -->|flow| bb_002D2E0F
  bb_002D2E0F -->|branch| bb_002D2E03
```
