# PnprLockPagesForReplace

- RVA: `0x0073A150`–`0x0073A179` (길이 `41` bytes)
- VA: `0x000000014073A150`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0073A15B` → [MmLockPagableSectionByHandle](../A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (function, `0x00A4D1E0`)
- `0x0073A16E` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (function, `0x003926B0`)

### Direct callers
- [PnprQuiesce](../../text/5A/PnprQuiesce_function_005A8DE8.md) at `0x005A8E70`
- [PnpReplacePartitionUnit](PnpReplacePartitionUnit_function_00738550.md) at `0x00738AE9`
- [PnprQuiesceWorker](../../pagelk/B6/PnprQuiesceWorker_function_00B654E0.md) at `0x00B65561`

### Static image references
- `0x0073A154` → RVA `0x00FC6C00` (`ALMOSTRO`; read)
- `0x0073A160` → RVA `0x00EFEDA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0073A16E` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0073A150  48 83 EC 28                     sub rsp, 0x28
0073A154  48 8B 0D A5 CA 88 00            mov rcx, qword ptr [rip + 0x88caa5]
0073A15B  E8 80 30 31 00                  call 0x140a4d1e0
0073A160  48 8B 0D 41 4C 7C 00            mov rcx, qword ptr [rip + 0x7c4c41]
0073A167  45 33 C0                        xor r8d, r8d
0073A16A  41 8D 50 03                     lea edx, [r8 + 3]
0073A16E  E8 3D 85 C5 FF                  call 0x1403926b0
0073A173  48 83 C4 28                     add rsp, 0x28
0073A177  C3                              ret
0073A178  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnprLockPagesForReplace(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MmLockPagableSectionByHandle(*(unsigned __int64 *)(v_rip + 8964773), a2, a3, a4);
    a3 = 0;
    result = ExNotifyCallback(*(unsigned __int64 *)(v_rip + 8145985), a3 + 3, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnprLockPagesForReplace(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MmLockPagableSectionByHandle(*(uint64_t *)(v_rip + 0x88CAA5), Arg2, Arg3, a4);
    Arg3 = 0;
    result = ExNotifyCallback(*(uint64_t *)(v_rip + 0x7C4C41), Arg3 + 3, Arg3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0073A150&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0073A150[BB_0073A150]
  bb_0073A178[BB_0073A178]
```
