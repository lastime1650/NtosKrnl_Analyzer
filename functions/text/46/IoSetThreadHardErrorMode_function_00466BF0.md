# IoSetThreadHardErrorMode

- RVA: `0x00466BF0`–`0x00466C1B` (길이 `43` bytes)
- VA: `0x0000000140466BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **20**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SmKmEtwAppendObjectName](../60/SmKmEtwAppendObjectName_function_0060F6D8.md) at `0x0060F772`
- [SmKmEtwAppendObjectName](../60/SmKmEtwAppendObjectName_function_0060F6D8.md) at `0x0060F7A4`
- [SmKmFileInfoGetPath](../../page/7A/SmKmFileInfoGetPath_function_007A83AC.md) at `0x007A83EF`
- [SmKmFileInfoGetPath](../../page/7A/SmKmFileInfoGetPath_function_007A83AC.md) at `0x007A8453`
- [SmKmIsVolumeIoPossible](../../page/7A/SmKmIsVolumeIoPossible_function_007A84BC.md) at `0x007A84E8`
- [SmKmIsVolumeIoPossible](../../page/7A/SmKmIsVolumeIoPossible_function_007A84BC.md) at `0x007A8574`
- [SmKmStoreFileCreate](../../page/7A/SmKmStoreFileCreate_function_007A8F14.md) at `0x007A8FEF`
- [SmKmStoreFileCreate](../../page/7A/SmKmStoreFileCreate_function_007A8F14.md) at `0x007A9393`
- [SmKmStoreFileCreateForIoType](../../page/7A/SmKmStoreFileCreateForIoType_function_007A93C8.md) at `0x007A9458`
- [SmKmStoreFileCreateForIoType](../../page/7A/SmKmStoreFileCreateForIoType_function_007A93C8.md) at `0x007A961F`
- [SmKmStoreFileDelete](../../page/7A/SmKmStoreFileDelete_function_007A9680.md) at `0x007A969C`
- [SmKmStoreFileDelete](../../page/7A/SmKmStoreFileDelete_function_007A9680.md) at `0x007A96FB`
- [SmKmStoreFileGetExtents](../../page/7A/SmKmStoreFileGetExtents_function_007A971C.md) at `0x007A9792`
- [SmKmStoreFileGetExtents](../../page/7A/SmKmStoreFileGetExtents_function_007A971C.md) at `0x007A9953`
- [SmKmStoreFileOpenVolume](../../page/7A/SmKmStoreFileOpenVolume_function_007A9C14.md) at `0x007A9C80`
- [SmKmStoreFileOpenVolume](../../page/7A/SmKmStoreFileOpenVolume_function_007A9C14.md) at `0x007A9D80`
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9E06`
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9FAF`
- [SmKmVolumeQueryUniqueId](../../page/7A/SmKmVolumeQueryUniqueId_function_007A9FE8.md) at `0x007AA007`
- [SmKmVolumeQueryUniqueId](../../page/7A/SmKmVolumeQueryUniqueId_function_007A9FE8.md) at `0x007AA057`
- [EtwpPsProvCaptureState](../../page/7C/EtwpPsProvCaptureState_function_007C0AD4.md) at `0x007C0B07`
- [EtwpPsProvCaptureState](../../page/7C/EtwpPsProvCaptureState_function_007C0AD4.md) at `0x007C0B32`
- [CmpCmdHiveOpen](../../page/87/CmpCmdHiveOpen_function_00878404.md) at `0x00878467`
- [CmpCmdHiveOpen](../../page/87/CmpCmdHiveOpen_function_00878404.md) at `0x008784F5`
- [EtwTraceProcess](../../page/8A/EtwTraceProcess_function_008A4004.md) at `0x008A4197`
- [EtwTraceProcess](../../page/8A/EtwTraceProcess_function_008A4004.md) at `0x008A41B1`
- [ObKillProcess](../../page/90/ObKillProcess_function_00904F30.md) at `0x00904F50`
- [ObKillProcess](../../page/90/ObKillProcess_function_00904F30.md) at `0x00904F67`
- [FsRtlSetFileSize](../../page/98/FsRtlSetFileSize_function_00982B04.md) at `0x00982B6C`
- [FsRtlSetFileSize](../../page/98/FsRtlSetFileSize_function_00982B04.md) at `0x00982BFD`
- [FsRtlGetFileSize](../../page/98/FsRtlGetFileSize_function_00985150.md) at `0x0098523D`
- [FsRtlGetFileSize](../../page/98/FsRtlGetFileSize_function_00985150.md) at `0x009852CE`
- [CmpDoFileSetSizeEx](../../page/9B/CmpDoFileSetSizeEx_function_009B2A4C.md) at `0x009B2AF0`
- [CmpDoFileSetSizeEx](../../page/9B/CmpDoFileSetSizeEx_function_009B2A4C.md) at `0x009B2B42`
- [CmpCmdHiveClose](../../page/9B/CmpCmdHiveClose_function_009B3948.md) at `0x009B398B`
- [CmpCmdHiveClose](../../page/9B/CmpCmdHiveClose_function_009B3948.md) at `0x009B3A74`
- [EtwpKernelTraceRundown](../../page/9E/EtwpKernelTraceRundown_function_009E4080.md) at `0x009E40B3`
- [EtwpKernelTraceRundown](../../page/9E/EtwpKernelTraceRundown_function_009E4080.md) at `0x009E444A`
- [SmKmFileInfoCleanup](../../page/AC/SmKmFileInfoCleanup_function_00AC9A90.md) at `0x00AC9A9F`
- [SmKmFileInfoCleanup](../../page/AC/SmKmFileInfoCleanup_function_00AC9A90.md) at `0x00AC9B1B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00466BF0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00466BF9  84 C9                           test cl, cl
00466BFB  74 13                           je 0x140466c10
00466BFD  F0 0F BA B0 A0 05 00 00 04      lock btr dword ptr [rax + 0x5a0], 4
00466C06  0F 92 C0                        setb al
00466C09  84 C0                           test al, al
00466C0B  0F 94 C0                        sete al
00466C0E  C3                              ret
00466C0F  CC                              int3
00466C10  F0 0F BA A8 A0 05 00 00 04      lock bts dword ptr [rax + 0x5a0], 4
00466C19  EB EB                           jmp 0x140466c06
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSetThreadHardErrorMode(unsigned __int8 a1)
{
    __int64 result;

    if (a1 == 0) goto loc_00466C10;
loc_00466C06:
    result = (condition_is_below) ? 1 : 0;
    result = ((unsigned __int8)(result) == 0) ? 1 : 0;
    return result;
loc_00466C10:
    goto loc_00466C06;
}
```

## 5. (Beta) C Style

```c
int64_t IoSetThreadHardErrorMode(uint8_t Arg1)
{
    int64_t result;

    if (Arg1 == 0) goto loc_00466C10;
loc_00466C06:
    result = (condition_is_below) ? 1 : 0;
    result = ((uint8_t)(result) == 0) ? 1 : 0;
    return result;
loc_00466C10:
    goto loc_00466C06;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00466BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00466BF0[BB_00466BF0]
  bb_00466BFD[BB_00466BFD]
  bb_00466C06[BB_00466C06]
  bb_00466C0F[BB_00466C0F]
  bb_00466C10[BB_00466C10]
  bb_00466BF0 -->|branch| bb_00466C10
  bb_00466BF0 -->|fallthrough| bb_00466BFD
  bb_00466BFD -->|flow| bb_00466C06
  bb_00466C0F -->|flow| bb_00466C10
  bb_00466C10 -->|branch| bb_00466C06
```
