# RtlEnoughStackSpaceForStackCapture

- RVA: `0x004341D0`–`0x00434215` (길이 `69` bytes)
- VA: `0x00000001404341D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BAC`
- 디코드: `21`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004341EC` → [RtlpGetStackLimits](../2F/RtlpGetStackLimits_function_002F5F50.md) (function, `0x002F5F50`)
- `0x004341F5` → [KeGetCurrentStackPointer](../6B/KeGetCurrentStackPointer_function_006B1070.md) (function, `0x006B1070`)

### Direct callers
- [IovpLogStackTrace](../../pagevrfy/BB/IovpLogStackTrace_function_00BB6A5C.md) at `0x00BB6AD7`
- [ViPtCaptureStackTrace](../../pagevrfy/BB/ViPtCaptureStackTrace_function_00BB7314.md) at `0x00BB7338`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004341D0  40 53                           push rbx
004341D2  48 83 EC 20                     sub rsp, 0x20
004341D6  33 DB                           xor ebx, ebx
004341D8  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
004341DD  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
004341E2  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
004341E7  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
004341EC  E8 5F 1D EC FF                  call 0x1402f5f50
004341F1  84 C0                           test al, al
004341F3  74 1C                           je 0x140434211
004341F5  E8 76 CE 27 00                  call 0x1406b1070
004341FA  48 2B 44 24 30                  sub rax, qword ptr [rsp + 0x30]
004341FF  48 3D 30 0E 00 00               cmp rax, 0xe30
00434205  0F 93 C3                        setae bl
00434208  8B C3                           mov eax, ebx
0043420A  48 83 C4 20                     add rsp, 0x20
0043420E  5B                              pop rbx
0043420F  C3                              ret
00434210  CC                              int3
00434211  33 C0                           xor eax, eax
00434213  EB F5                           jmp 0x14043420a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlEnoughStackSpaceForStackCapture(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    v_stack_p10 = 0;
    v_stack_p8 = 0;
    result = RtlpGetStackLimits(v_stack_p8, v_stack_p10, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00434211;
    result = KeGetCurrentStackPointer(v_stack_p8, v_stack_p10, a3, a4);
    result = (result) - (v_stack_p8);
    v_rbx = (result >= 0xE30ULL) ? 1 : 0;
loc_0043420A:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
loc_00434211:
    result = 0;
    goto loc_0043420A;
}
```

## 5. (Beta) C Style

```c
void RtlEnoughStackSpaceForStackCapture(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    v_stack_p10 = 0;
    v_stack_p8 = 0;
    result = RtlpGetStackLimits(v_stack_p8, v_stack_p10, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00434211;
    result = KeGetCurrentStackPointer(v_stack_p8, v_stack_p10, a3, a4);
    result = (result) - (v_stack_p8);
    local_rbx = (result >= 0xE30ULL) ? 1 : 0;
loc_0043420A:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
loc_00434211:
    result = 0;
    goto loc_0043420A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004341D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004341D0[BB_004341D0]
  bb_004341F5[BB_004341F5]
  bb_0043420A[BB_0043420A]
  bb_00434210[BB_00434210]
  bb_00434211[BB_00434211]
  bb_004341D0 -->|branch| bb_00434211
  bb_004341D0 -->|fallthrough| bb_004341F5
  bb_004341F5 -->|flow| bb_0043420A
  bb_00434210 -->|flow| bb_00434211
  bb_00434211 -->|branch| bb_0043420A
```
