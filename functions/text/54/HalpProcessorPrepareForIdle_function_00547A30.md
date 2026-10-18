# HalpProcessorPrepareForIdle

- RVA: `0x00547A30`–`0x00547A6F` (길이 `63` bytes)
- VA: `0x0000000140547A30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `16`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00547A62` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00547A52` → RVA `0x00E03B20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00547A30  48 83 EC 28                     sub rsp, 0x28
00547A34  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00547A3D  83 78 60 00                     cmp dword ptr [rax + 0x60], 0
00547A41  7E 24                           jle 0x140547a67
00547A43  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00547A4C  F6 40 60 01                     test byte ptr [rax + 0x60], 1
00547A50  75 15                           jne 0x140547a67
00547A52  48 8B 05 C7 C0 8B 00            mov rax, qword ptr [rip + 0x8bc0c7]
00547A59  48 8B 40 48                     mov rax, qword ptr [rax + 0x48]
00547A5D  48 85 C0                        test rax, rax
00547A60  74 05                           je 0x140547a67
00547A62  E8 69 30 17 00                  call 0x1406baad0
00547A67  33 C0                           xor eax, eax
00547A69  48 83 C4 28                     add rsp, 0x28
00547A6D  C3                              ret
00547A6E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpProcessorPrepareForIdle(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 96)) <= 0) goto loc_00547A67;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 96)) & (1)) != 0) goto loc_00547A67;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9158855) + 72);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9158855) + 72) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpProcessorPrepareForIdle(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x60)) <= 0) goto loc_00547A67;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x60)) & (1)) != 0) goto loc_00547A67;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8BC0C7) + 0x48);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8BC0C7) + 0x48) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00547A30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00547A30[BB_00547A30]
  bb_00547A43[BB_00547A43]
  bb_00547A52[BB_00547A52]
  bb_00547A62[BB_00547A62]
  bb_00547A67[BB_00547A67]
  bb_00547A6E[BB_00547A6E]
  bb_00547A30 -->|branch| bb_00547A67
  bb_00547A30 -->|fallthrough| bb_00547A43
  bb_00547A43 -->|branch| bb_00547A67
  bb_00547A43 -->|fallthrough| bb_00547A52
  bb_00547A52 -->|branch| bb_00547A67
  bb_00547A52 -->|fallthrough| bb_00547A62
  bb_00547A62 -->|flow| bb_00547A67
```
