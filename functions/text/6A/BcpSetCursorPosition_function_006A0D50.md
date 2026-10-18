# BcpSetCursorPosition

- RVA: `0x006A0D50`–`0x006A0D6C` (길이 `28` bytes)
- VA: `0x00000001406A0D50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [BcpDisplayCriticalCharacter](../69/BcpDisplayCriticalCharacter_function_0069F678.md) at `0x0069F733`
- [BcpDisplayCriticalString](../69/BcpDisplayCriticalString_function_0069F754.md) at `0x0069FA98`
- [BcpDisplayCriticalStringCentered](../69/BcpDisplayCriticalStringCentered_function_0069FAB8.md) at `0x0069FB87`
- [BcpDisplayCriticalStringCentered](../69/BcpDisplayCriticalStringCentered_function_0069FAB8.md) at `0x0069FBF4`
- [BcpDisplayCriticalStringCentered](../69/BcpDisplayCriticalStringCentered_function_0069FAB8.md) at `0x0069FE4E`
- [BcpDisplayErrorInformation](../69/BcpDisplayErrorInformation_function_0069FE74.md) at `0x0069FF2E`
- [BcpDisplayErrorInformation](../69/BcpDisplayErrorInformation_function_0069FE74.md) at `0x0069FF5E`
- [BcpDisplayErrorInformation](../69/BcpDisplayErrorInformation_function_0069FE74.md) at `0x0069FFB2`
- [BcpDisplayErrorInformation](../69/BcpDisplayErrorInformation_function_0069FE74.md) at `0x006A002B`
- [BcpDisplayErrorInformation](../69/BcpDisplayErrorInformation_function_0069FE74.md) at `0x006A007C`
- [BcpDisplayErrorInformation](../69/BcpDisplayErrorInformation_function_0069FE74.md) at `0x006A009F`
- [BcpDisplayErrorInformationModernized](BcpDisplayErrorInformationModernized_function_006A00DC.md) at `0x006A0336`
- [BcpDisplayErrorInformationModernized](BcpDisplayErrorInformationModernized_function_006A00DC.md) at `0x006A0368`
- [BcpDisplayErrorInformationModernized](BcpDisplayErrorInformationModernized_function_006A00DC.md) at `0x006A038D`
- [BcpDisplayErrorInformationModernized](BcpDisplayErrorInformationModernized_function_006A00DC.md) at `0x006A03D2`
- [BcpDisplayErrorInformationModernized](BcpDisplayErrorInformationModernized_function_006A00DC.md) at `0x006A0423`
- [BcpDisplayErrorInformationModernized](BcpDisplayErrorInformationModernized_function_006A00DC.md) at `0x006A0447`
- [BcpGetComponentOffsets](BcpGetComponentOffsets_function_006A08C8.md) at `0x006A09BB`
- [BgpDisplaySafeToPowerOffScreen](BgpDisplaySafeToPowerOffScreen_function_006A0D74.md) at `0x006A0DEC`
- [BgpFwDisplayBugCheckProgressUpdate](BgpFwDisplayBugCheckProgressUpdate_function_006A0E1C.md) at `0x006A0EEC`
- [BgpFwDisplayBugCheckScreen](BgpFwDisplayBugCheckScreen_function_006A0FE8.md) at `0x006A10C9`
- [BgpFwDisplayBugCheckScreen](BgpFwDisplayBugCheckScreen_function_006A0FE8.md) at `0x006A1118`
- [BgpFwDisplayBugCheckScreen](BgpFwDisplayBugCheckScreen_function_006A0FE8.md) at `0x006A122C`
- [BgpFwDisplayBugCheckScreen](BgpFwDisplayBugCheckScreen_function_006A0FE8.md) at `0x006A128D`
- [BgpFwDisplayBugCheckScreenModernized](BgpFwDisplayBugCheckScreenModernized_function_006A1338.md) at `0x006A146D`
- [BgpFwDisplayBugCheckScreenModernized](BgpFwDisplayBugCheckScreenModernized_function_006A1338.md) at `0x006A158B`
- [BgpFwDisplayBugCheckScreenModernized](BgpFwDisplayBugCheckScreenModernized_function_006A1338.md) at `0x006A15EE`
- [BgpFwDisplayBugCheckScreenModernized](BgpFwDisplayBugCheckScreenModernized_function_006A1338.md) at `0x006A162E`
- [BgpFwDisplayBugCheckScreenModernized](BgpFwDisplayBugCheckScreenModernized_function_006A1338.md) at `0x006A16EC`
- [BgpFwDisplayBugCheckScreenModernized](BgpFwDisplayBugCheckScreenModernized_function_006A1338.md) at `0x006A1752`
- [BgpFwDisplayBugCheckScreenModernized](BgpFwDisplayBugCheckScreenModernized_function_006A1338.md) at `0x006A1796`

### Static image references
- `0x006A0D50` → RVA `0x00EEFEF8` (`.data`; write)
- `0x006A0D56` → RVA `0x00EEFEFC` (`.data`; write)
- `0x006A0D64` → RVA `0x00EEFF00` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A0D50  89 0D A2 F1 84 00               mov dword ptr [rip + 0x84f1a2], ecx
006A0D56  89 15 A0 F1 84 00               mov dword ptr [rip + 0x84f1a0], edx
006A0D5C  4D 85 C0                        test r8, r8
006A0D5F  74 09                           je 0x1406a0d6a
006A0D61  41 8B 00                        mov eax, dword ptr [r8]
006A0D64  89 05 96 F1 84 00               mov dword ptr [rip + 0x84f196], eax
006A0D6A  C3                              ret
006A0D6B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BcpSetCursorPosition(int a1, int a2, __int64 a3)
{
    __int64 result;

    *(unsigned int *)(v_rip + 8712610) = a1;
    *(unsigned int *)(v_rip + 8712608) = a2;
    if (a3 != 0) {
        result = *(unsigned int *)(a3);
        *(unsigned int *)(v_rip + 8712598) = (unsigned int)(result);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BcpSetCursorPosition(int32_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;

    *(uint32_t *)(v_rip + 0x84F1A2) = Arg1;
    *(uint32_t *)(v_rip + 0x84F1A0) = Arg2;
    if (Arg3 != 0) {
        result = *(uint32_t *)(Arg3);
        *(uint32_t *)(v_rip + 0x84F196) = (uint32_t)(result);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A0D50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A0D50[BB_006A0D50]
  bb_006A0D61[BB_006A0D61]
  bb_006A0D6A[BB_006A0D6A]
  bb_006A0D6B[BB_006A0D6B]
  bb_006A0D50 -->|branch| bb_006A0D6A
  bb_006A0D50 -->|fallthrough| bb_006A0D61
  bb_006A0D61 -->|flow| bb_006A0D6A
```
