# ExpLicUpdateChecksum

- RVA: `0x006578AC`–`0x006578C4` (길이 `24` bytes)
- VA: `0x00000001406578AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExpGetLicenseTamperState](ExpGetLicenseTamperState_function_00657740.md) at `0x00657801`
- [ExpGetLicenseTamperState](ExpGetLicenseTamperState_function_00657740.md) at `0x00657832`
- [sub_007C7FB0](../../page/7C/Unknown_function_007C7FB0.md) at `0x007C81E2`
- [sub_007C7FB0](../../page/7C/Unknown_function_007C7FB0.md) at `0x007C8213`
- [SLUpdateLicenseDataInternal](../../page/7C/SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007C9FB1`
- [SLUpdateLicenseDataInternal](../../page/7C/SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007C9FE7`
- [SLUpdateLicenseDataInternal](../../page/7C/SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007CA604`
- [SLUpdateLicenseDataInternal](../../page/7C/SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007CA63A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006578AC  33 C0                           xor eax, eax
006578AE  48 85 C9                        test rcx, rcx
006578B1  74 0A                           je 0x1406578bd
006578B3  4D 85 C0                        test r8, r8
006578B6  74 05                           je 0x1406578bd
006578B8  49 89 00                        mov qword ptr [r8], rax
006578BB  C3                              ret
006578BC  CC                              int3
006578BD  B8 0D 00 00 C0                  mov eax, 0xc000000d
006578C2  C3                              ret
006578C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpLicUpdateChecksum(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    result = 0;
    if (a1 == 0) goto loc_006578BD;
    if (a3 == 0) goto loc_006578BD;
    *(unsigned __int64 *)(a3) = 0;
    return result;
loc_006578BD:
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t ExpLicUpdateChecksum(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;

    result = 0;
    if (Arg1 == 0) goto loc_006578BD;
    if (Arg3 == 0) goto loc_006578BD;
    *(uint64_t *)(Arg3) = 0;
    return result;
loc_006578BD:
    return (uint32_t)(0xC000000DULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006578AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006578AC[BB_006578AC]
  bb_006578B3[BB_006578B3]
  bb_006578B8[BB_006578B8]
  bb_006578BC[BB_006578BC]
  bb_006578BD[BB_006578BD]
  bb_006578C3[BB_006578C3]
  bb_006578AC -->|branch| bb_006578BD
  bb_006578AC -->|fallthrough| bb_006578B3
  bb_006578B3 -->|branch| bb_006578BD
  bb_006578B3 -->|fallthrough| bb_006578B8
  bb_006578BC -->|flow| bb_006578BD
```
