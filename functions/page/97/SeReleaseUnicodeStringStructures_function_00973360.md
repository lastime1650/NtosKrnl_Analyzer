# SeReleaseUnicodeStringStructures

- RVA: `0x00973360`–`0x0097337B` (길이 `27` bytes)
- VA: `0x0000000140973360`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00973370` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SepCaptureUnicodeStringArray](SepCaptureUnicodeStringArray_function_00972F70.md) at `0x00973135`
- [SepCaptureUnicodeStringArray](SepCaptureUnicodeStringArray_function_00972F70.md) at `0x00973197`
- [SepCaptureUnicodeStringArray](SepCaptureUnicodeStringArray_function_00972F70.md) at `0x009731D4`
- [SepCaptureUnicodeStringArray](SepCaptureUnicodeStringArray_function_00972F70.md) at `0x009731E9`
- [SepCaptureUnicodeStringArray](SepCaptureUnicodeStringArray_function_00972F70.md) at `0x009731FD`
- [NtQuerySecurityPolicy](NtQuerySecurityPolicy_function_00973410.md) at `0x00973601`
- [NtQuerySecurityPolicy](NtQuerySecurityPolicy_function_00973410.md) at `0x0097360E`
- [NtQuerySecurityPolicy](NtQuerySecurityPolicy_function_00973410.md) at `0x0097361B`
- [NtSetCachedSigningLevel2](NtSetCachedSigningLevel2_function_00973720.md) at `0x0097380B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00973370` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00973360  48 83 EC 28                     sub rsp, 0x28
00973364  80 FA 01                        cmp dl, 1
00973367  75 0C                           jne 0x140973375
00973369  48 85 C9                        test rcx, rcx
0097336C  74 07                           je 0x140973375
0097336E  33 D2                           xor edx, edx
00973370  E8 FB F4 20 00                  call 0x140b82870
00973375  48 83 C4 28                     add rsp, 0x28
00973379  C3                              ret
0097337A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeReleaseUnicodeStringStructures(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned __int8)(a2)) != 1) goto loc_00973375;
    if (a1 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeReleaseUnicodeStringStructures(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint8_t)(Arg2)) != 1) goto loc_00973375;
    if (Arg1 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00973360&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00973360[BB_00973360]
  bb_00973369[BB_00973369]
  bb_0097336E[BB_0097336E]
  bb_00973375[BB_00973375]
  bb_0097337A[BB_0097337A]
  bb_00973360 -->|branch| bb_00973375
  bb_00973360 -->|fallthrough| bb_00973369
  bb_00973369 -->|branch| bb_00973375
  bb_00973369 -->|fallthrough| bb_0097336E
  bb_0097336E -->|flow| bb_00973375
```
