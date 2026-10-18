# Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting

- RVA: `0x00222FE0`–`0x00222FE7` (길이 `7` bytes)
- VA: `0x0000000140222FE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `7/7` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwTraceAutoBoostProcessLockEntry](EtwTraceAutoBoostProcessLockEntry_function_00221C7C.md) at `0x00221CAA`
- [EtwTraceAutoBoostSetFloor](EtwTraceAutoBoostSetFloor_function_00222EF0.md) at `0x00222F63`
- [EtwTraceAutoBoostConvertWaiterToOwner](../4D/EtwTraceAutoBoostConvertWaiterToOwner_function_004DAF98.md) at `0x004DAFC6`
- [PspUpdateJobEffectivePriorityLimits](../../page/87/PspUpdateJobEffectivePriorityLimits_function_0087EAD4.md) at `0x0087EB45`
- [MiCommitPageTablesForVad](../../page/88/MiCommitPageTablesForVad_function_00886D50.md) at `0x00887068`
- [MiCommitPageTablesForVad](../../page/88/MiCommitPageTablesForVad_function_00886D50.md) at `0x00887097`
- [NtSetInformationThread](../../page/8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA727`
- [MiComputeProcessUserVa](../../page/8C/MiComputeProcessUserVa_function_008CFB8C.md) at `0x008CFBD3`
- [sub_009E5A2C](../../page/9E/Unknown_function_009E5A2C.md) at `0x009E5A37`
- [MiUnloadSystemImage](../../page/AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA32E5`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6BB1`
- [sub_00C7EB3D](../../init/C7/Unknown_function_00C7EB3D.md) at `0x00C7EC4D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00222FE0  B8 01 00 00 00                  mov eax, 1
00222FE5  C3                              ret
00222FE6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting(void)
{
    return 1;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting(void)
{
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00222FE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00222FE0[BB_00222FE0]
  bb_00222FE6[BB_00222FE6]
```
