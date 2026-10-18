# Feature_OpocksAndMappedSections__private_ReportDeviceUsage

- RVA: `0x0046BC88`–`0x0046BCEB` (길이 `99` bytes)
- VA: `0x000000014046BC88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009AE6C`
- 디코드: `23`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0046BCCE` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x0046BCE4` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)

### Direct callers
- [FsRtlCheckOplockForFsFilterCallback](../../page/9F/FsRtlCheckOplockForFsFilterCallback_function_009F67A0.md) at `0x009F67E9`

### Static image references
- `0x0046BC92` → RVA `0x00FC4710` (`.data`; read)
- `0x0046BCBE` → RVA `0x000DD390` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046BC88  48 83 EC 28                     sub rsp, 0x28
0046BC8C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0046BC92  8B 0D 78 8A B5 00               mov ecx, dword ptr [rip + 0xb58a78]
0046BC98  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0046BC9C  F6 C1 10                        test cl, 0x10
0046BC9F  74 06                           je 0x14046bca7
0046BCA1  48 83 C4 28                     add rsp, 0x28
0046BCA5  C3                              ret
0046BCA6  CC                              int3
0046BCA7  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0046BCAC  41 B9 01 00 00 00               mov r9d, 1
0046BCB2  41 0B C9                        or ecx, r9d
0046BCB5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0046BCBA  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0046BCBE  48 8D 0D CB 16 C7 FF            lea rcx, [rip - 0x38e935]
0046BCC5  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0046BCCA  45 8D 41 02                     lea r8d, [r9 + 2]
0046BCCE  E8 11 2A 0D 00                  call 0x14053e6e4
0046BCD3  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0046BCD8  4C 8D 05 B1 16 C7 FF            lea r8, [rip - 0x38e94f]
0046BCDF  BA 03 00 00 00                  mov edx, 3
0046BCE4  E8 8B 2A 0D 00                  call 0x14053e774
0046BCE9  EB B6                           jmp 0x14046bca1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_OpocksAndMappedSections__private_ReportDeviceUsage(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11897464)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11897464)))) & (16)) == 0) goto loc_0046BCA7;
loc_0046BCA1:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0046BCA7:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11897464))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (unsigned int)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3729717, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3729743, 1);
    goto loc_0046BCA1;
}
```

## 5. (Beta) C Style

```c
void Feature_OpocksAndMappedSections__private_ReportDeviceUsage(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB58A78)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB58A78)))) & (16)) == 0) goto loc_0046BCA7;
loc_0046BCA1:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0046BCA7:
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB58A78))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (uint32_t)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3729717, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3729743, 1);
    goto loc_0046BCA1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046BC88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046BC88[BB_0046BC88]
  bb_0046BCA1[BB_0046BCA1]
  bb_0046BCA6[BB_0046BCA6]
  bb_0046BCA7[BB_0046BCA7]
  bb_0046BC88 -->|branch| bb_0046BCA7
  bb_0046BC88 -->|fallthrough| bb_0046BCA1
  bb_0046BCA6 -->|flow| bb_0046BCA7
  bb_0046BCA7 -->|branch| bb_0046BCA1
```
