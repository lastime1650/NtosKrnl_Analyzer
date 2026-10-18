# MmForceSectionClosed

- RVA: `0x004838D0`–`0x0048391B` (길이 `75` bytes)
- VA: `0x00000001404838D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009F34C`
- 디코드: `27`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004838EB` → [MiForceSectionClosed](../2A/MiForceSectionClosed_function_002ACFD4.md) (function, `0x002ACFD4`)
- `0x00483914` → [MiForceSectionClosed](../2A/MiForceSectionClosed_function_002ACFD4.md) (function, `0x002ACFD4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004838D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004838D5  57                              push rdi
004838D6  48 83 EC 20                     sub rsp, 0x20
004838DA  F6 DA                           neg dl
004838DC  48 8B F9                        mov rdi, rcx
004838DF  1B DB                           sbb ebx, ebx
004838E1  45 33 C0                        xor r8d, r8d
004838E4  83 E3 04                        and ebx, 4
004838E7  FF C3                           inc ebx
004838E9  8B D3                           mov edx, ebx
004838EB  E8 E4 96 E2 FF                  call 0x1402acfd4
004838F0  85 C0                           test eax, eax
004838F2  74 12                           je 0x140483906
004838F4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004838F9  83 F8 02                        cmp eax, 2
004838FC  0F 95 C0                        setne al
004838FF  48 83 C4 20                     add rsp, 0x20
00483903  5F                              pop rdi
00483904  C3                              ret
00483905  CC                              int3
00483906  83 E3 FE                        and ebx, 0xfffffffe
00483909  45 33 C0                        xor r8d, r8d
0048390C  83 CB 02                        or ebx, 2
0048390F  48 8B CF                        mov rcx, rdi
00483912  8B D3                           mov edx, ebx
00483914  E8 BB 96 E2 FF                  call 0x1402acfd4
00483919  EB D9                           jmp 0x1404838f4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmForceSectionClosed(__int64 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a2 = (unsigned __int8)(-(a2));
    a3 = 0;
    v_rbx = (unsigned int)((v_rbx) & (4));
    v_rbx = (unsigned int)((v_rbx) + 1);
    result = MiForceSectionClosed(a1, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00483906;
loc_004838F4:
    result = (((unsigned int)(result)) != 2) ? 1 : 0;
    v_rsp = (v_rsp) + (32);
    return result;
loc_00483906:
    v_rbx = (unsigned int)((v_stack_p8) & (0xFFFFFFFEULL));
    a3 = 0;
    v_rbx = (unsigned int)((v_rbx) | (2));
    result = MiForceSectionClosed(a1, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    goto loc_004838F4;
}
```

## 5. (Beta) C Style

```c
int64_t MmForceSectionClosed(int64_t Arg1, uint8_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg2 = (uint8_t)(-(Arg2));
    Arg3 = 0;
    local_rbx = (uint32_t)((local_rbx) & (4));
    local_rbx = (uint32_t)((local_rbx) + 1);
    result = MiForceSectionClosed(Arg1, (uint32_t)((uint32_t)(local_rbx)), Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_00483906;
loc_004838F4:
    result = (((uint32_t)(result)) != 2) ? 1 : 0;
    local_rsp = (local_rsp) + (32);
    return result;
loc_00483906:
    local_rbx = (uint32_t)((v_stack_p8) & (0xFFFFFFFEULL));
    Arg3 = 0;
    local_rbx = (uint32_t)((local_rbx) | (2));
    result = MiForceSectionClosed(Arg1, (uint32_t)((uint32_t)(local_rbx)), Arg3, a4);
    goto loc_004838F4;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004838D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004838D0[BB_004838D0]
  bb_004838F4[BB_004838F4]
  bb_00483905[BB_00483905]
  bb_00483906[BB_00483906]
  bb_004838D0 -->|branch| bb_00483906
  bb_004838D0 -->|fallthrough| bb_004838F4
  bb_00483905 -->|flow| bb_00483906
  bb_00483906 -->|branch| bb_004838F4
```
