# RtlpRecordBootStatusData

- RVA: `0x00A8F57C`–`0x00A8F5C4` (길이 `72` bytes)
- VA: `0x0000000140A8F57C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `20`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A8F5B9` → [ZwPowerInformation](../../text/6A/ZwPowerInformation_function_006ADCB0.md) (function, `0x006ADCB0`)

### Direct callers
- [RtlInitializeBootStatusDataBlackBox](../79/RtlInitializeBootStatusDataBlackBox_function_00790694.md) at `0x00790726`
- [RtlRestoreBootStatusDefaults](../79/RtlRestoreBootStatusDefaults_function_00790758.md) at `0x007907EA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A8F5B9` → [ZwPowerInformation](../../text/6A/ZwPowerInformation_function_006ADCB0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8F57C  4C 8B DC                        mov r11, rsp
00A8F57F  48 83 EC 58                     sub rsp, 0x58
00A8F583  33 C0                           xor eax, eax
00A8F585  49 C7 43 F0 01 00 00 00         mov qword ptr [r11 - 0x10], 1
00A8F58D  49 89 53 D8                     mov qword ptr [r11 - 0x28], rdx
00A8F591  4D 89 4B E0                     mov qword ptr [r11 - 0x20], r9
00A8F595  4D 89 43 E8                     mov qword ptr [r11 - 0x18], r8
00A8F599  84 C9                           test cl, cl
00A8F59B  74 07                           je 0x140a8f5a4
00A8F59D  83 C8 01                        or eax, 1
00A8F5A0  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00A8F5A4  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00A8F5A9  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00A8F5AE  45 33 C9                        xor r9d, r9d
00A8F5B1  45 8D 41 20                     lea r8d, [r9 + 0x20]
00A8F5B5  41 8D 49 5E                     lea ecx, [r9 + 0x5e]
00A8F5B9  E8 F2 E6 C1 FF                  call 0x1406adcb0
00A8F5BE  48 83 C4 58                     add rsp, 0x58
00A8F5C2  C3                              ret
00A8F5C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpRecordBootStatusData(unsigned __int8 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m38;
    unsigned int v_stack_mC;

    v_rsp = (v_rsp) - (88);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 16) = 1;
    *(unsigned __int64 *)(v_rsp - 40) = a2;
    *(unsigned __int64 *)(v_rsp - 32) = a4;
    *(unsigned __int64 *)(v_rsp - 24) = a3;
    if (a1 != 0) {
        result = (unsigned int)((result) | (1));
        v_stack_mC = (unsigned int)(result);
    }
    a4 = 0;
    result = ZwPowerInformation(a4 + 94, v_stack_m28, a4 + 32, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpRecordBootStatusData(uint8_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m38;
    uint32_t v_stack_mC;

    local_rsp = (local_rsp) - (88);
    result = 0;
    *(uint64_t *)(local_rsp - 0x10) = 1;
    *(uint64_t *)(local_rsp - 0x28) = Arg2;
    *(uint64_t *)(local_rsp - 0x20) = Arg4;
    *(uint64_t *)(local_rsp - 0x18) = Arg3;
    if (Arg1 != 0) {
        result = (uint32_t)((result) | (1));
        v_stack_mC = (uint32_t)(result);
    }
    Arg4 = 0;
    result = ZwPowerInformation(Arg4 + 94, v_stack_m28, Arg4 + 32, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8F57C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8F57C[BB_00A8F57C]
  bb_00A8F59D[BB_00A8F59D]
  bb_00A8F5A4[BB_00A8F5A4]
  bb_00A8F5C3[BB_00A8F5C3]
  bb_00A8F57C -->|branch| bb_00A8F5A4
  bb_00A8F57C -->|fallthrough| bb_00A8F59D
  bb_00A8F59D -->|flow| bb_00A8F5A4
```
