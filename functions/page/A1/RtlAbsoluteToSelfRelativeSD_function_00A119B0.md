# RtlAbsoluteToSelfRelativeSD

- RVA: `0x00A119B0`–`0x00A119CD` (길이 `29` bytes)
- VA: `0x0000000140A119B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A119BB` → [RtlMakeSelfRelativeSD](RtlMakeSelfRelativeSD_function_00A119D4.md) (function, `0x00A119D4`)

### Direct callers
- [SepCheckAndCopySelfRelativeSD](../../text/4B/SepCheckAndCopySelfRelativeSD_function_004B596C.md) at `0x004B59CB`
- [sub_006FBBCC](../../text/6F/Unknown_function_006FBBCC.md) at `0x006FBBD7`
- [PiAuGetServiceStateSecurityObject](../73/PiAuGetServiceStateSecurityObject_function_007314F0.md) at `0x007316EC`
- [PiAuGetStateDirectorySecurityObject](../73/PiAuGetStateDirectorySecurityObject_function_00731738.md) at `0x007319CC`
- [CMFCreateSecurityDescriptor](../7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D3067`
- [CMFCreateSecurityDescriptor](../7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D30A5`
- [CmpGenerateAppHiveSecurityDescriptor](../7E/CmpGenerateAppHiveSecurityDescriptor_function_007ECEAC.md) at `0x007ED080`
- [CmpGenerateAppHiveSecurityDescriptor](../7E/CmpGenerateAppHiveSecurityDescriptor_function_007ECEAC.md) at `0x007ED0AE`
- [PnpGetEnumSecurityDescriptor](../83/PnpGetEnumSecurityDescriptor_function_00831FCC.md) at `0x00832297`
- [DrvDbGetRegistrarSecurityDescriptor](../83/DrvDbGetRegistrarSecurityDescriptor_function_00835728.md) at `0x008357DA`
- [DrvDbGetSecurityDescriptor](../83/DrvDbGetSecurityDescriptor_function_0083580C.md) at `0x00835B27`
- [PiDevCfgGetKeySecurityDescriptor](../99/PiDevCfgGetKeySecurityDescriptor_function_00996240.md) at `0x00996575`
- [_PnpGetPropertiesSecurityDescriptor](../A9/_PnpGetPropertiesSecurityDescriptor_function_00A91B8C.md) at `0x00A91D28`
- [sub_00B4403A](../B4/Unknown_function_00B4403A.md) at `0x00B4410B`
- [PiAuCreateLocalSystemSecurityObject](../../init/C3/PiAuCreateLocalSystemSecurityObject_function_00C34570.md) at `0x00C346BC`
- [PiAuCreateStandardSecurityObject](../../init/C3/PiAuCreateStandardSecurityObject_function_00C34710.md) at `0x00C34C06`
- [PiAuGetDriverDataDirectorySecurityObject](../../init/C3/PiAuGetDriverDataDirectorySecurityObject_function_00C34EEC.md) at `0x00C350D1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A119B0  48 83 EC 28                     sub rsp, 0x28
00A119B4  66 83 79 02 00                  cmp word ptr [rcx + 2], 0
00A119B9  7C 0B                           jl 0x140a119c6
00A119BB  E8 14 00 00 00                  call 0x140a119d4
00A119C0  48 83 C4 28                     add rsp, 0x28
00A119C4  C3                              ret
00A119C5  CC                              int3
00A119C6  B8 E7 00 00 C0                  mov eax, 0xc00000e7
00A119CB  EB F3                           jmp 0x140a119c0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlAbsoluteToSelfRelativeSD(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int16 *)(a1 + 2)) < 0) goto loc_00A119C6;
    result = RtlMakeSelfRelativeSD(a1, a2, a3, a4);
loc_00A119C0:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A119C6:
    goto loc_00A119C0;
}
```

## 5. (Beta) C Style

```c
int64_t RtlAbsoluteToSelfRelativeSD(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint16_t *)(arg1 + 0x2)) < 0) goto loc_00A119C6;
    result = RtlMakeSelfRelativeSD(Arg1, a2, a3, a4);
loc_00A119C0:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A119C6:
    goto loc_00A119C0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A119B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A119B0[BB_00A119B0]
  bb_00A119BB[BB_00A119BB]
  bb_00A119C0[BB_00A119C0]
  bb_00A119C5[BB_00A119C5]
  bb_00A119C6[BB_00A119C6]
  bb_00A119B0 -->|branch| bb_00A119C6
  bb_00A119B0 -->|fallthrough| bb_00A119BB
  bb_00A119BB -->|flow| bb_00A119C0
  bb_00A119C5 -->|flow| bb_00A119C6
  bb_00A119C6 -->|branch| bb_00A119C0
```
