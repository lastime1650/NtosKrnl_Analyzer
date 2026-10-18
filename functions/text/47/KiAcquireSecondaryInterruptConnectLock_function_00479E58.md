# KiAcquireSecondaryInterruptConnectLock

- RVA: `0x00479E58`–`0x00479EA7` (길이 `79` bytes)
- VA: `0x0000000140479E58`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068908`
- 디코드: `23`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00479E88` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x00479EA0` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [KiDisconnectInterruptCommon](../2D/KiDisconnectInterruptCommon_function_002D36A8.md) at `0x002D386F`
- [KiDisconnectSecondaryInterrupt](../2D/KiDisconnectSecondaryInterrupt_function_002D3B88.md) at `0x002D3BCE`
- [KiConnectSecondaryInterrupt](../2D/KiConnectSecondaryInterrupt_function_002D4200.md) at `0x002D4280`
- [KiUnmaskSecondaryInterruptInternal](KiUnmaskSecondaryInterruptInternal_function_00479CC8.md) at `0x00479D03`
- [KiMaskSecondaryInterruptInternal](KiMaskSecondaryInterruptInternal_function_00479D94.md) at `0x00479DCA`

### Static image references
- `0x00479E7A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00479E58  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00479E5D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00479E62  57                              push rdi
00479E63  48 83 EC 20                     sub rsp, 0x20
00479E67  48 8B FA                        mov rdi, rdx
00479E6A  48 8B F1                        mov rsi, rcx
00479E6D  44 0F 20 C3                     mov rbx, cr8
00479E71  BA 0C 00 00 00                  mov edx, 0xc
00479E76  44 0F 22 C2                     mov cr8, rdx
00479E7A  83 3D 9F CE B4 00 00            cmp dword ptr [rip + 0xb4ce9f], 0
00479E81  75 1B                           jne 0x140479e9e
00479E83  48 8B CE                        mov rcx, rsi
00479E86  88 1F                           mov byte ptr [rdi], bl
00479E88  E8 A3 E5 D8 FF                  call 0x140208430
00479E8D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00479E92  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00479E97  48 83 C4 20                     add rsp, 0x20
00479E9B  5F                              pop rdi
00479E9C  C3                              ret
00479E9D  CC                              int3
00479E9E  8A CB                           mov cl, bl
00479EA0  E8 57 B8 07 00                  call 0x1404f56fc
00479EA5  EB DC                           jmp 0x140479e83
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAcquireSecondaryInterruptConnectLock(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 11849375)) != 0) goto loc_00479E9E;
loc_00479E83:
    *(unsigned __int8 *)(a2) = (unsigned __int8)(v_cr8);
    result = KeAcquireSpinLockAtDpcLevel(a1, 12, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00479E9E:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p8), 12, a3, a4);
    goto loc_00479E83;
}
```

## 5. (Beta) C Style

```c
int64_t KiAcquireSecondaryInterruptConnectLock(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xB4CE9F)) != 0) goto loc_00479E9E;
loc_00479E83:
    *(uint8_t *)(arg2) = (uint8_t)(v_cr8);
    result = KeAcquireSpinLockAtDpcLevel(Arg1, 12, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00479E9E:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p8), 12, a3, a4);
    goto loc_00479E83;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00479E58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00479E58[BB_00479E58]
  bb_00479E83[BB_00479E83]
  bb_00479E9D[BB_00479E9D]
  bb_00479E9E[BB_00479E9E]
  bb_00479E58 -->|branch| bb_00479E9E
  bb_00479E58 -->|fallthrough| bb_00479E83
  bb_00479E9D -->|flow| bb_00479E9E
  bb_00479E9E -->|branch| bb_00479E83
```
