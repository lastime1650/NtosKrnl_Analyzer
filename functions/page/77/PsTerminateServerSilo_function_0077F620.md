# PsTerminateServerSilo

- RVA: `0x0077F620`–`0x0077F640` (길이 `32` bytes)
- VA: `0x000000014077F620`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0077F629` → [PsIsServerSilo](../../text/22/PsIsServerSilo_function_00225828.md) (function, `0x00225828`)
- `0x0077F635` → [PspTerminateAllProcessesInJobHierarchy](../91/PspTerminateAllProcessesInJobHierarchy_function_00917B7C.md) (function, `0x00917B7C`)

### Direct callers
- [PspInitializeServerSiloDeferred](PspInitializeServerSiloDeferred_function_0077FEE0.md) at `0x007800F7`
- [PsShutdownSystem](../78/PsShutdownSystem_function_00785E94.md) at `0x00785F1F`
- [PspCatchCriticalBreak](../78/PspCatchCriticalBreak_function_00786408.md) at `0x00786575`
- [NtSetSystemPowerState](../../pagelk/B7/NtSetSystemPowerState_function_00B70890.md) at `0x00B7097A`
- [ExpSystemErrorHandler2](../../pagelk/B7/ExpSystemErrorHandler2_function_00B72C30.md) at `0x00B73269`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0077F629` → [PsIsServerSilo](../../text/22/PsIsServerSilo_function_00225828.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077F620  48 83 EC 28                     sub rsp, 0x28
0077F624  48 85 C9                        test rcx, rcx
0077F627  74 11                           je 0x14077f63a
0077F629  E8 FA 61 AA FF                  call 0x140225828
0077F62E  84 C0                           test al, al
0077F630  74 08                           je 0x14077f63a
0077F632  45 33 C0                        xor r8d, r8d
0077F635  E8 42 85 19 00                  call 0x140917b7c
0077F63A  48 83 C4 28                     add rsp, 0x28
0077F63E  C3                              ret
0077F63F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsTerminateServerSilo(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) goto loc_0077F63A;
    result = PsIsServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a3 = 0;
        result = PspTerminateAllProcessesInJobHierarchy(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsTerminateServerSilo(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) goto loc_0077F63A;
    result = PsIsServerSilo(Arg1, Arg2, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg3 = 0;
        result = PspTerminateAllProcessesInJobHierarchy(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077F620&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077F620[BB_0077F620]
  bb_0077F629[BB_0077F629]
  bb_0077F632[BB_0077F632]
  bb_0077F63A[BB_0077F63A]
  bb_0077F63F[BB_0077F63F]
  bb_0077F620 -->|branch| bb_0077F63A
  bb_0077F620 -->|fallthrough| bb_0077F629
  bb_0077F629 -->|branch| bb_0077F63A
  bb_0077F629 -->|fallthrough| bb_0077F632
  bb_0077F632 -->|flow| bb_0077F63A
```
