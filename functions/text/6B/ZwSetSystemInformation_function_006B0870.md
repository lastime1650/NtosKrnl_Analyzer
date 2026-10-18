# ZwSetSystemInformation

- RVA: `0x006B0870`–`0x006B088F` (길이 `31` bytes)
- VA: `0x00000001406B0870`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C136C`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SmKmStoreTerminateWorker](../60/SmKmStoreTerminateWorker_function_0060FB30.md) at `0x0060FDAA`
- [DifZwSetSystemInformationWrapper](../64/DifZwSetSystemInformationWrapper_function_0064AF70.md) at `0x0064B054`
- [SmStoreCreate](../../page/7A/SmStoreCreate_function_007A7198.md) at `0x007A7268`
- [SmStoreDelete](../../page/7A/SmStoreDelete_function_007A72A0.md) at `0x007A7317`
- [SmStoreResize](../../page/7A/SmStoreResize_function_007A748C.md) at `0x007A7524`
- [NtSetSystemInformation](../../page/AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF4F75`
- [IoShutdownSystem](../../pagelk/B6/IoShutdownSystem_function_00B63B8C.md) at `0x00B63C1A`
- [IoShutdownSystem](../../pagelk/B6/IoShutdownSystem_function_00B63B8C.md) at `0x00B63CFE`
- [KitpInitAitSampleRate](../../init/C5/KitpInitAitSampleRate_function_00C53FC8.md) at `0x00C5402E`

### Static image references
- `0x006B087C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B0889` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B0870  48 8B C4                        mov rax, rsp
006B0873  FA                              cli
006B0874  48 83 EC 10                     sub rsp, 0x10
006B0878  50                              push rax
006B0879  9C                              pushfq
006B087A  6A 10                           push 0x10
006B087C  48 8D 05 DD 2B 00 00            lea rax, [rip + 0x2bdd]
006B0883  50                              push rax
006B0884  B8 BD 01 00 00                  mov eax, 0x1bd
006B0889  E9 32 41 01 00                  jmp 0x1406c49c0
006B088E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwSetSystemInformation(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwSetSystemInformation(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B0870&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006B0870[BB_006B0870]
  bb_006B088E[BB_006B088E]
```
