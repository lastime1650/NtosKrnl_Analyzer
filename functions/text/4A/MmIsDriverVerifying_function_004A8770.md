# MmIsDriverVerifying

- RVA: `0x004A8770`–`0x004A878E` (길이 `30` bytes)
- VA: `0x00000001404A8770`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **19**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IopCompleteUnloadOrDelete](../27/IopCompleteUnloadOrDelete_function_00270BC8.md) at `0x00270CD9`
- [VfDifCaptureIoCallbacks](VfDifCaptureIoCallbacks_function_004A8698.md) at `0x004A86AA`
- [VfDifCaptureDriverEntry](VfDifCaptureDriverEntry_function_004A86F8.md) at `0x004A870E`
- [sub_006FC1AC](../6F/Unknown_function_006FC1AC.md) at `0x006FC1BB`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089EEF0`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A0732`
- [IopGetBasicInformationFile](../../page/8A/IopGetBasicInformationFile_function_008AC038.md) at `0x008AC0EB`
- [NtQueryInformationFile](../../page/8A/NtQueryInformationFile_function_008AD630.md) at `0x008ADCDA`
- [IopReadFile](../../page/8A/IopReadFile_function_008AEFF0.md) at `0x008AF46C`
- [IopWriteFile](../../page/8E/IopWriteFile_function_008E9790.md) at `0x008E9A21`
- [IopXxxControlFile](../../page/8E/IopXxxControlFile_function_008E9AD0.md) at `0x008EB0A2`
- [IopQueryInformation](../../page/9D/IopQueryInformation_function_009D8370.md) at `0x009D856F`
- [NtLockFile](../../page/9D/NtLockFile_function_009D86D0.md) at `0x009D8CED`
- [NtUnlockFile](../../page/9E/NtUnlockFile_function_009E5DA0.md) at `0x009E625D`
- [sub_00B174A6](../../page/B1/Unknown_function_00B174A6.md) at `0x00B17555`
- [VfGetPristineDispatchRoutine](../../pagevrfy/B9/VfGetPristineDispatchRoutine_function_00B9D87C.md) at `0x00B9D894`
- [VfGetPristineDriverInit](../../pagevrfy/B9/VfGetPristineDriverInit_function_00B9D8CC.md) at `0x00B9D8D5`
- [IovUtilIsVerifiedDeviceStack](../../pagevrfy/BA/IovUtilIsVerifiedDeviceStack_function_00BA2B88.md) at `0x00BA2BE1`
- [VfDevObjPreAddDevice](../../pagevrfy/BB/VfDevObjPreAddDevice_function_00BB963C.md) at `0x00BB964F`
- [VfDevObjPostAddDevice](../../pagevrfy/BB/VfDevObjPostAddDevice_function_00BB9688.md) at `0x00BB96AC`

### Static image references
- `0x004A8772` → RVA `0x00E681A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A8770  33 C0                           xor eax, eax
004A8772  39 05 28 FA 9B 00               cmp dword ptr [rip + 0x9bfa28], eax
004A8778  74 12                           je 0x1404a878c
004A877A  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
004A877E  48 85 C9                        test rcx, rcx
004A8781  74 09                           je 0x1404a878c
004A8783  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
004A8786  C1 E8 19                        shr eax, 0x19
004A8789  83 E0 01                        and eax, 1
004A878C  C3                              ret
004A878D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmIsDriverVerifying(__int64 a1)
{
    __int64 result;

    result = 0;
    if ((*(unsigned int *)(v_rip + 10222120)) == 0) goto loc_004A878C;
    if (*(unsigned __int64 *)(a1 + 40) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 104);
        result = (unsigned int)((result) >> (25));
        result = (unsigned int)((result) & (1));
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmIsDriverVerifying(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 0;
    if ((*(uint32_t *)(v_rip + 0x9BFA28)) == 0) goto loc_004A878C;
    if (*(uint64_t *)(arg1 + 0x28) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x68);
        result = (uint32_t)((result) >> (25));
        result = (uint32_t)((result) & (1));
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A8770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A8770[BB_004A8770]
  bb_004A877A[BB_004A877A]
  bb_004A8783[BB_004A8783]
  bb_004A878C[BB_004A878C]
  bb_004A878D[BB_004A878D]
  bb_004A8770 -->|branch| bb_004A878C
  bb_004A8770 -->|fallthrough| bb_004A877A
  bb_004A877A -->|branch| bb_004A878C
  bb_004A877A -->|fallthrough| bb_004A8783
  bb_004A8783 -->|flow| bb_004A878C
```
