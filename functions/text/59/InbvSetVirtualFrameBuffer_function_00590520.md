# InbvSetVirtualFrameBuffer

- RVA: `0x00590520`–`0x0059054E` (길이 `46` bytes)
- VA: `0x0000000140590520`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0059053C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00590524` → RVA `0x00E65E58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00590520  48 83 EC 28                     sub rsp, 0x28
00590524  48 8B 05 2D 59 8D 00            mov rax, qword ptr [rip + 0x8d592d]
0059052B  48 85 C0                        test rax, rax
0059052E  74 13                           je 0x140590543
00590530  48 8B 80 B0 00 00 00            mov rax, qword ptr [rax + 0xb0]
00590537  48 85 C0                        test rax, rax
0059053A  74 07                           je 0x140590543
0059053C  E8 8F A5 12 00                  call 0x1406baad0
00590541  EB 05                           jmp 0x140590548
00590543  B8 02 00 00 C0                  mov eax, 0xc0000002
00590548  48 83 C4 28                     add rsp, 0x28
0059054C  C3                              ret
0059054D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InbvSetVirtualFrameBuffer(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 9263405) == 0) goto loc_00590543;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9263405) + 176) == 0) goto loc_00590543;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_00590548;
loc_00590543:
loc_00590548:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC0000002ULL);
}
```

## 5. (Beta) C Style

```c
void InbvSetVirtualFrameBuffer(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x8D592D) == 0) goto loc_00590543;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D592D) + 0xB0) == 0) goto loc_00590543;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_00590548;
loc_00590543:
loc_00590548:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC0000002ULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00590520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00590520[BB_00590520]
  bb_00590530[BB_00590530]
  bb_0059053C[BB_0059053C]
  bb_00590543[BB_00590543]
  bb_00590548[BB_00590548]
  bb_0059054D[BB_0059054D]
  bb_00590520 -->|branch| bb_00590543
  bb_00590520 -->|fallthrough| bb_00590530
  bb_00590530 -->|branch| bb_00590543
  bb_00590530 -->|fallthrough| bb_0059053C
  bb_0059053C -->|branch| bb_00590548
  bb_00590543 -->|flow| bb_00590548
```
