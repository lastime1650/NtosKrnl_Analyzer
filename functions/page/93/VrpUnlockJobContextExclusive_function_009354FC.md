# VrpUnlockJobContextExclusive

- RVA: `0x009354FC`–`0x00935531` (길이 `53` bytes)
- VA: `0x00000001409354FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00935518` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00935520` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00935525` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [VrpHandleIoctlCreateMultipleNamespaceNodes](../83/VrpHandleIoctlCreateMultipleNamespaceNodes_function_0083B17C.md) at `0x0083B428`
- [VrpHandleIoctlModifyFlags](../83/VrpHandleIoctlModifyFlags_function_0083B69C.md) at `0x0083B769`
- [VrpHandleIoctlCreateNamespaceNode](VrpHandleIoctlCreateNamespaceNode_function_0093511C.md) at `0x00935313`
- [VrpHandleIoctlLoadDifferencingHive](VrpHandleIoctlLoadDifferencingHive_function_00935C5C.md) at `0x00935EC6`
- [VrpHandleIoctlLoadDifferencingHive](VrpHandleIoctlLoadDifferencingHive_function_00935C5C.md) at `0x00935F30`
- [VrpHandleIoctlUnloadDynamicallyLoadedHives](VrpHandleIoctlUnloadDynamicallyLoadedHives_function_0093778C.md) at `0x009378D1`
- [VrpHandleIoctlUnloadDynamicallyLoadedHives](VrpHandleIoctlUnloadDynamicallyLoadedHives_function_0093778C.md) at `0x009378E5`
- [VrpPreUnloadKey](VrpPreUnloadKey_function_00937950.md) at `0x0093798C`
- [VrpPreUnloadKey](VrpPreUnloadKey_function_00937950.md) at `0x009379A2`
- [VrpPreLoadKey](../A8/VrpPreLoadKey_function_00A8A43C.md) at `0x00A8A845`
- [VrpPostUnloadKey](../AD/VrpPostUnloadKey_function_00AD60DC.md) at `0x00AD612C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00935518` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00935520` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00935525` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009354FC  40 53                           push rbx
009354FE  48 83 EC 20                     sub rsp, 0x20
00935502  48 8D 59 10                     lea rbx, [rcx + 0x10]
00935506  48 83 C8 FF                     or rax, 0xffffffffffffffff
0093550A  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
0093550F  24 06                           and al, 6
00935511  3C 02                           cmp al, 2
00935513  75 08                           jne 0x14093551d
00935515  48 8B CB                        mov rcx, rbx
00935518  E8 B3 08 93 FF                  call 0x140265dd0
0093551D  48 8B CB                        mov rcx, rbx
00935520  E8 DB C0 9A FF                  call 0x1402e1600
00935525  E8 86 83 92 FF                  call 0x14025d8b0
0093552A  48 83 C4 20                     add rsp, 0x20
0093552E  5B                              pop rbx
0093552F  C3                              ret
00935530  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpUnlockJobContextExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 16;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 16, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 16, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VrpUnlockJobContextExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 + 16;
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1 + 16, a2, a3, a4);
    result = KeLeaveCriticalRegion(Arg1 + 16, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009354FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009354FC[BB_009354FC]
  bb_00935515[BB_00935515]
  bb_0093551D[BB_0093551D]
  bb_00935530[BB_00935530]
  bb_009354FC -->|branch| bb_0093551D
  bb_009354FC -->|fallthrough| bb_00935515
  bb_00935515 -->|flow| bb_0093551D
```
