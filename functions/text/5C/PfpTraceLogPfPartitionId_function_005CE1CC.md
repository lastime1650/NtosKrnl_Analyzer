# PfpTraceLogPfPartitionId

- RVA: `0x005CE1CC`–`0x005CE1E5` (길이 `25` bytes)
- VA: `0x00000001405CE1CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005CE1DA` → [PfpTraceLogPartitionId](PfpTraceLogPartitionId_function_005CE1B0.md) (function, `0x005CE1B0`)

### Direct callers
- [PfTCleanup](../../page/75/PfTCleanup_function_00751208.md) at `0x0075125C`
- [PfTCleanup](../../page/75/PfTCleanup_function_00751208.md) at `0x00751451`
- [PfTStart](../../page/75/PfTStart_function_007517AC.md) at `0x00751808`
- [PfTStart](../../page/75/PfTStart_function_007517AC.md) at `0x00751B26`
- [PfDeletePartition](../../page/75/PfDeletePartition_function_00751EB4.md) at `0x00751F09`
- [PfDeletePartition](../../page/75/PfDeletePartition_function_00751EB4.md) at `0x00751FA0`
- [sub_00B20874](../../page/B2/Unknown_function_00B20874.md) at `0x00B20877`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CE1CC  48 83 EC 28                     sub rsp, 0x28
005CE1D0  33 C0                           xor eax, eax
005CE1D2  48 85 C9                        test rcx, rcx
005CE1D5  74 08                           je 0x1405ce1df
005CE1D7  48 8B 09                        mov rcx, qword ptr [rcx]
005CE1DA  E8 D1 FF FF FF                  call 0x1405ce1b0
005CE1DF  48 83 C4 28                     add rsp, 0x28
005CE1E3  C3                              ret
005CE1E4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpTraceLogPfPartitionId(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (a1 != 0) {
        a1 = *(unsigned __int64 *)(a1);
        result = PfpTraceLogPartitionId(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfpTraceLogPfPartitionId(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (Arg1 != 0) {
        Arg1 = *(uint64_t *)(Arg1);
        result = PfpTraceLogPartitionId(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CE1CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CE1CC[BB_005CE1CC]
  bb_005CE1D7[BB_005CE1D7]
  bb_005CE1DF[BB_005CE1DF]
  bb_005CE1E4[BB_005CE1E4]
  bb_005CE1CC -->|branch| bb_005CE1DF
  bb_005CE1CC -->|fallthrough| bb_005CE1D7
  bb_005CE1D7 -->|flow| bb_005CE1DF
```
