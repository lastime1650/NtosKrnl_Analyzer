# ZwPlugPlayControl

- RVA: `0x006AF890`–`0x006AF8AF` (길이 `31` bytes)
- VA: `0x00000001406AF890`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0D78`
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
- [PiPnpRtlGatherDeviceDeleteInfo](../../page/72/PiPnpRtlGatherDeviceDeleteInfo_function_0072FC04.md) at `0x0072FCA0`
- [PiCMDeleteDeviceWorker](../../page/73/PiCMDeleteDeviceWorker_function_0073B420.md) at `0x0073B59D`
- [PiCMSetProblem](../../page/73/PiCMSetProblem_function_0073B9E4.md) at `0x0073BAA6`
- [PiPnpRtlGetDeviceInterfaceEnabled](../../page/9F/PiPnpRtlGetDeviceInterfaceEnabled_function_009F4310.md) at `0x009F433A`
- [PiPnpRtlGetDeviceStatus](../../page/9F/PiPnpRtlGetDeviceStatus_function_009FE7A0.md) at `0x009FE805`
- [PlugPlayGetDeviceProperty](../../page/A2/PlugPlayGetDeviceProperty_function_00A2CBD0.md) at `0x00A2CC32`
- [PiPnpRtlGetDeviceRelatedDeviceRoutine](../../page/A2/PiPnpRtlGetDeviceRelatedDeviceRoutine_function_00A2CC90.md) at `0x00A2CCE8`
- [PiPnpRtlGetDeviceRelationsList](../../page/A6/PiPnpRtlGetDeviceRelationsList_function_00A6DD50.md) at `0x00A6DD99`

### Static image references
- `0x006AF89C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AF8A9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AF890  48 8B C4                        mov rax, rsp
006AF893  FA                              cli
006AF894  48 83 EC 10                     sub rsp, 0x10
006AF898  50                              push rax
006AF899  9C                              pushfq
006AF89A  6A 10                           push 0x10
006AF89C  48 8D 05 BD 3B 00 00            lea rax, [rip + 0x3bbd]
006AF8A3  50                              push rax
006AF8A4  B8 3E 01 00 00                  mov eax, 0x13e
006AF8A9  E9 12 51 01 00                  jmp 0x1406c49c0
006AF8AE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwPlugPlayControl(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwPlugPlayControl(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AF890&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AF890[BB_006AF890]
  bb_006AF8AE[BB_006AF8AE]
```
