# PsChargePoolQuota

- RVA: `0x003EC7F0`–`0x003EC80B` (길이 `27` bytes)
- VA: `0x00000001403EC7F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009654C`
- 디코드: `10`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003EC7F4` → [PsChargeProcessPoolQuota](PsChargeProcessPoolQuota_function_003EC820.md) (function, `0x003EC820`)
- `0x003EC805` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- [FsRtlCancelNotify](../4E/FsRtlCancelNotify_function_004E7F90.md) at `0x004E81CC`
- [FsRtlNotifyFilterReportChange](../../page/A1/FsRtlNotifyFilterReportChange_function_00A1E880.md) at `0x00A1EB41`
- [FsRtlNotifyFilterReportChangeLiteEx](../../page/A1/FsRtlNotifyFilterReportChangeLiteEx_function_00A1F2B0.md) at `0x00A1F7DD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EC7F0  48 83 EC 28                     sub rsp, 0x28
003EC7F4  E8 27 00 00 00                  call 0x1403ec820
003EC7F9  85 C0                           test eax, eax
003EC7FB  78 06                           js 0x1403ec803
003EC7FD  48 83 C4 28                     add rsp, 0x28
003EC801  C3                              ret
003EC802  CC                              int3
003EC803  8B C8                           mov ecx, eax
003EC805  E8 46 A2 F0 FF                  call 0x1402f6a50
003EC80A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsChargePoolQuota(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsChargeProcessPoolQuota(a1, a2, a3, a4);
    if (sign_flag) goto loc_003EC803;
    v_rsp = (v_rsp) + (40);
    return result;
loc_003EC803:
    result = RtlRaiseStatus((unsigned int)((unsigned int)(result)), a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
void PsChargePoolQuota(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsChargeProcessPoolQuota(a1, a2, a3, a4);
    if (sign_flag) goto loc_003EC803;
    local_rsp = (local_rsp) + (40);
    return result;
loc_003EC803:
    result = RtlRaiseStatus((uint32_t)((uint32_t)(result)), a2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EC7F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EC7F0[BB_003EC7F0]
  bb_003EC7FD[BB_003EC7FD]
  bb_003EC802[BB_003EC802]
  bb_003EC803[BB_003EC803]
  bb_003EC7F0 -->|branch| bb_003EC803
  bb_003EC7F0 -->|fallthrough| bb_003EC7FD
  bb_003EC802 -->|flow| bb_003EC803
```
