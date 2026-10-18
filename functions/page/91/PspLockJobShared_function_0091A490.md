# PspLockJobShared

- RVA: `0x0091A490`–`0x0091A4B2` (길이 `34` bytes)
- VA: `0x000000014091A490`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0091A4A7` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)

### Direct callers
- [PspCompleteServerSiloShutdownDeferred](../77/PspCompleteServerSiloShutdownDeferred_function_0077F860.md) at `0x0077F954`
- [PspQueryJobHierarchyInterferenceCount](../78/PspQueryJobHierarchyInterferenceCount_function_00785110.md) at `0x00785137`
- [PspQueryJobHierarchyProcessIdList](PspQueryJobHierarchyProcessIdList_function_0091854C.md) at `0x00918588`
- [PspCallJobHierarchyCallbacks](PspCallJobHierarchyCallbacks_function_00918A34.md) at `0x00918BD0`
- [NtQueryInformationJobObject](../9F/NtQueryInformationJobObject_function_009FB860.md) at `0x009FC108`
- [NtQueryInformationJobObject](../9F/NtQueryInformationJobObject_function_009FB860.md) at `0x009FC280`
- [NtQueryInformationJobObject](../9F/NtQueryInformationJobObject_function_009FB860.md) at `0x009FC2F2`
- [sub_00B21AB8](../B2/Unknown_function_00B21AB8.md) at `0x00B21AF1`
- [sub_00B307F0](../B3/Unknown_function_00B307F0.md) at `0x00B307FF`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B31785`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B31821`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B319DA`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B31A47`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B31AEB`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B31CC8`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B32476`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B324BD`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B3251D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0091A4A7` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0091A490  48 83 EC 28                     sub rsp, 0x28
0091A494  48 85 D2                        test rdx, rdx
0091A497  74 08                           je 0x14091a4a1
0091A499  66 FF 8A E6 01 00 00            dec word ptr [rdx + 0x1e6]
0091A4A0  90                              nop
0091A4A1  48 83 C1 38                     add rcx, 0x38
0091A4A5  B2 01                           mov dl, 1
0091A4A7  E8 14 77 8F FF                  call 0x140211bc0
0091A4AC  48 83 C4 28                     add rsp, 0x28
0091A4B0  C3                              ret
0091A4B1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspLockJobShared(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 != 0) {
    }
    a1 = (a1) + (56);
    result = ExAcquireResourceSharedLite(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspLockJobShared(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 != 0) {
    }
    Arg1 = (Arg1) + (56);
    result = ExAcquireResourceSharedLite(Arg1, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091A490&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0091A490[BB_0091A490]
  bb_0091A499[BB_0091A499]
  bb_0091A4A1[BB_0091A4A1]
  bb_0091A4B1[BB_0091A4B1]
  bb_0091A490 -->|branch| bb_0091A4A1
  bb_0091A490 -->|fallthrough| bb_0091A499
  bb_0091A499 -->|flow| bb_0091A4A1
```
