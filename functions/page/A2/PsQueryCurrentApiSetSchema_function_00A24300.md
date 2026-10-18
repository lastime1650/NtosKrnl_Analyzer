# PsQueryCurrentApiSetSchema

- RVA: `0x00A24300`–`0x00A2433E` (길이 `62` bytes)
- VA: `0x0000000140A24300`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C74`
- 디코드: `16`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A2430A` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00A2431D` → [MmQueryApiSetSchema](../../text/4C/MmQueryApiSetSchema_function_004C013C.md) (function, `0x004C013C`)
- `0x00A24330` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [RtlIsApiSetImplemented](../79/RtlIsApiSetImplemented_function_00792C30.md) at `0x00792C3E`
- [ExIsMultiSessionSku](../7C/ExIsMultiSessionSku_function_007C7538.md) at `0x007C758A`
- [MiResolveImageReferences](MiResolveImageReferences_function_00A23BE4.md) at `0x00A23D37`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A2430A` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00A2431D` → [MmQueryApiSetSchema](../../text/4C/MmQueryApiSetSchema_function_004C013C.md) (`PAGE` → `.text`)
  - `0x00A24330` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A24300  48 83 EC 28                     sub rsp, 0x28
00A24304  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00A2430A  E8 D1 1F A1 FF                  call 0x1404362e0
00A2430F  84 C0                           test al, al
00A24311  75 1D                           jne 0x140a24330
00A24313  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00A24318  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00A2431D  E8 1A BE A9 FF                  call 0x1404c013c
00A24322  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00A24327  48 8B 00                        mov rax, qword ptr [rax]
00A2432A  48 83 C4 28                     add rsp, 0x28
00A2432E  C3                              ret
00A2432F  CC                              int3
00A24330  E8 BB 9E 8D FF                  call 0x1402fe1f0
00A24335  48 8B 80 F0 03 00 00            mov rax, qword ptr [rax + 0x3f0]
00A2433C  EB EC                           jmp 0x140a2432a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsQueryCurrentApiSetSchema(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A24330;
    result = MmQueryApiSetSchema(v_stack_p8, v_stack_p10, a3, a4);
loc_00A2432A:
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(v_stack_p8);
loc_00A24330:
    result = PsGetCurrentServerSiloGlobals(v_stack_p8, v_stack_p10, a3, a4);
    goto loc_00A2432A;
}
```

## 5. (Beta) C Style

```c
void PsQueryCurrentApiSetSchema(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A24330;
    result = MmQueryApiSetSchema(v_stack_p8, v_stack_p10, a3, a4);
loc_00A2432A:
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(v_stack_p8);
loc_00A24330:
    result = PsGetCurrentServerSiloGlobals(v_stack_p8, v_stack_p10, a3, a4);
    goto loc_00A2432A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A24300&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A24300[BB_00A24300]
  bb_00A24313[BB_00A24313]
  bb_00A2432A[BB_00A2432A]
  bb_00A2432F[BB_00A2432F]
  bb_00A24330[BB_00A24330]
  bb_00A24300 -->|branch| bb_00A24330
  bb_00A24300 -->|fallthrough| bb_00A24313
  bb_00A24313 -->|flow| bb_00A2432A
  bb_00A2432F -->|flow| bb_00A24330
  bb_00A24330 -->|branch| bb_00A2432A
```
