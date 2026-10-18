# KiAcquireProcessLockExclusive

- RVA: `0x003C26B8`–`0x003C2708` (길이 `80` bytes)
- VA: `0x00000001403C26B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068908`
- 디코드: `23`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003C26E9` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003C2701` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [KeSetProcessPpmPolicy](KeSetProcessPpmPolicy_function_003C1CCC.md) at `0x003C1CFE`
- [KeSetQuantumProcess](KeSetQuantumProcess_function_003C1EF0.md) at `0x003C1F1E`
- [KeSetExecuteOptions](KeSetExecuteOptions_function_003C1F54.md) at `0x003C1FA4`
- [KeSetDisableQuantumProcess](KeSetDisableQuantumProcess_function_003C2128.md) at `0x003C2145`
- [KeStartThread](KeStartThread_function_003C21B8.md) at `0x003C2251`
- [KeAdjustTimerDelayProcess](../5B/KeAdjustTimerDelayProcess_function_005B9658.md) at `0x005B968A`
- [KeRecomputeCpuSetAffinityProcess](../5C/KeRecomputeCpuSetAffinityProcess_function_005C1078.md) at `0x005C1091`
- [KeSetCpuSetsProcess](../5C/KeSetCpuSetsProcess_function_005C10D4.md) at `0x005C1118`
- [KeSetExpectedConcurrencyCountProcess](../5C/KeSetExpectedConcurrencyCountProcess_function_005C1AC0.md) at `0x005C1B06`

### Static image references
- `0x003C26DA` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C26B8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003C26BD  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
003C26C2  57                              push rdi
003C26C3  48 83 EC 20                     sub rsp, 0x20
003C26C7  48 8B FA                        mov rdi, rdx
003C26CA  48 8B F1                        mov rsi, rcx
003C26CD  44 0F 20 C3                     mov rbx, cr8
003C26D1  BA 02 00 00 00                  mov edx, 2
003C26D6  44 0F 22 C2                     mov cr8, rdx
003C26DA  83 3D 3F 46 C0 00 00            cmp dword ptr [rip + 0xc0463f], 0
003C26E1  75 1C                           jne 0x1403c26ff
003C26E3  48 8D 4E 40                     lea rcx, [rsi + 0x40]
003C26E7  88 1F                           mov byte ptr [rdi], bl
003C26E9  E8 92 67 E8 FF                  call 0x140248e80
003C26EE  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003C26F3  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003C26F8  48 83 C4 20                     add rsp, 0x20
003C26FC  5F                              pop rdi
003C26FD  C3                              ret
003C26FE  CC                              int3
003C26FF  8A CB                           mov cl, bl
003C2701  E8 F6 2F 13 00                  call 0x1404f56fc
003C2706  EB DB                           jmp 0x1403c26e3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAcquireProcessLockExclusive(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 12600895)) != 0) goto loc_003C26FF;
loc_003C26E3:
    *(unsigned __int8 *)(a2) = (unsigned __int8)(v_cr8);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1 + 64, 2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_003C26FF:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p8), 2, a3, a4);
    goto loc_003C26E3;
}
```

## 5. (Beta) C Style

```c
int64_t KiAcquireProcessLockExclusive(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xC0463F)) != 0) goto loc_003C26FF;
loc_003C26E3:
    *(uint8_t *)(arg2) = (uint8_t)(v_cr8);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1 + 64, 2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_003C26FF:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p8), 2, a3, a4);
    goto loc_003C26E3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C26B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003C26B8[BB_003C26B8]
  bb_003C26E3[BB_003C26E3]
  bb_003C26FE[BB_003C26FE]
  bb_003C26FF[BB_003C26FF]
  bb_003C26B8 -->|branch| bb_003C26FF
  bb_003C26B8 -->|fallthrough| bb_003C26E3
  bb_003C26FE -->|flow| bb_003C26FF
  bb_003C26FF -->|branch| bb_003C26E3
```
