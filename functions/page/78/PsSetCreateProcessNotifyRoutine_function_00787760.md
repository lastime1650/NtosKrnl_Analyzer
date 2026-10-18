# PsSetCreateProcessNotifyRoutine

- RVA: `0x00787760`–`0x00787778` (길이 `24` bytes)
- VA: `0x0000000140787760`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0078776D` → [PspSetCreateProcessNotifyRoutine](../AA/PspSetCreateProcessNotifyRoutine_function_00AA75EC.md) (function, `0x00AA75EC`)

### Direct callers
- [ViRlrsUnload](../../text/61/ViRlrsUnload_function_00617590.md) at `0x006175C1`
- [DifPsSetCreateProcessNotifyRoutineWrapper](../../text/63/DifPsSetCreateProcessNotifyRoutineWrapper_function_0063AC50.md) at `0x0063AD24`
- [VfInitSystemNoRebootNeeded](../../pagevrfy/B9/VfInitSystemNoRebootNeeded_function_00B93970.md) at `0x00B93A92`
- [VfFaultsInitPhase1](../../pagevrfy/BA/VfFaultsInitPhase1_function_00BA6458.md) at `0x00BA6465`
- [VfFaultsSetParameters](../../pagevrfy/BA/VfFaultsSetParameters_function_00BA67E4.md) at `0x00BA6831`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00787760  48 83 EC 28                     sub rsp, 0x28
00787764  8A C2                           mov al, dl
00787766  33 D2                           xor edx, edx
00787768  84 C0                           test al, al
0078776A  0F 95 C2                        setne dl
0078776D  E8 7A FE 31 00                  call 0x140aa75ec
00787772  48 83 C4 28                     add rsp, 0x28
00787776  C3                              ret
00787777  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsSetCreateProcessNotifyRoutine(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    a2 = ((unsigned __int8)((unsigned __int8)(a2)) != 0) ? 1 : 0;
    result = PspSetCreateProcessNotifyRoutine(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsSetCreateProcessNotifyRoutine(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    Arg2 = ((uint8_t)((uint8_t)(Arg2)) != 0) ? 1 : 0;
    result = PspSetCreateProcessNotifyRoutine(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00787760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00787760[BB_00787760]
  bb_00787777[BB_00787777]
```
