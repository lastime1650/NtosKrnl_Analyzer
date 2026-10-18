# ZwSetInformationThread

- RVA: `0x006AD270`–`0x006AD28F` (길이 `31` bytes)
- VA: `0x00000001406AD270`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFF2C`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExpWorkerFactoryCreateThread](../34/ExpWorkerFactoryCreateThread_function_0034B620.md) at `0x0034B75D`
- [ExpWorkerFactoryCreateThread](../34/ExpWorkerFactoryCreateThread_function_0034B620.md) at `0x0034B7E8`
- [DifZwSetInformationThreadWrapper](../64/DifZwSetInformationThreadWrapper_function_0064AAD0.md) at `0x0064ABC3`
- [DbgkUserReportWorkRoutine](../../page/71/DbgkUserReportWorkRoutine_function_00710D10.md) at `0x00710F54`
- [EtwpCovSampCaptureContextStart](../../page/7C/EtwpCovSampCaptureContextStart_function_007C14AC.md) at `0x007C174D`
- [RtlAcquirePrivilege](../../page/87/RtlAcquirePrivilege_function_00879120.md) at `0x008791EE`
- [RtlAcquirePrivilege](../../page/87/RtlAcquirePrivilege_function_00879120.md) at `0x0087931E`
- [RtlImpersonateSelfEx](../../page/87/RtlImpersonateSelfEx_function_008793A0.md) at `0x00879475`
- [BiReleasePrivilege](../../page/A3/BiReleasePrivilege_function_00A3D600.md) at `0x00A3D644`
- [BiAcquirePrivilege](../../page/A3/BiAcquirePrivilege_function_00A3D658.md) at `0x00A3D6FA`
- [RtlReleasePrivilege](../../page/A6/RtlReleasePrivilege_function_00A685A0.md) at `0x00A685F3`

### Static image references
- `0x006AD27C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD289` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD270  48 8B C4                        mov rax, rsp
006AD273  FA                              cli
006AD274  48 83 EC 10                     sub rsp, 0x10
006AD278  50                              push rax
006AD279  9C                              pushfq
006AD27A  6A 10                           push 0x10
006AD27C  48 8D 05 DD 61 00 00            lea rax, [rip + 0x61dd]
006AD283  50                              push rax
006AD284  B8 0D 00 00 00                  mov eax, 0xd
006AD289  E9 32 77 01 00                  jmp 0x1406c49c0
006AD28E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwSetInformationThread(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwSetInformationThread(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD270&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD270[BB_006AD270]
  bb_006AD28E[BB_006AD28E]
```
