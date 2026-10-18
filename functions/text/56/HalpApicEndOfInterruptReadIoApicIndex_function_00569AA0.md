# HalpApicEndOfInterruptReadIoApicIndex

- RVA: `0x00569AA0`–`0x00569ACB` (길이 `43` bytes)
- VA: `0x0000000140569AA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00569AC0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00569AB9` → RVA `0x00E10458` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00569AA0  48 83 EC 28                     sub rsp, 0x28
00569AA4  48 85 C9                        test rcx, rcx
00569AA7  74 10                           je 0x140569ab9
00569AA9  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00569AAD  48 85 C0                        test rax, rax
00569AB0  74 07                           je 0x140569ab9
00569AB2  90                              nop
00569AB3  8B 00                           mov eax, dword ptr [rax]
00569AB5  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00569AB9  48 8B 05 98 69 8A 00            mov rax, qword ptr [rip + 0x8a6998]
00569AC0  E8 0B 10 15 00                  call 0x1406baad0
00569AC5  48 83 C4 28                     add rsp, 0x28
00569AC9  C3                              ret
00569ACA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpApicEndOfInterruptReadIoApicIndex(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) goto loc_00569AB9;
    result = *(unsigned __int64 *)(a1 + 16);
    if (*(unsigned __int64 *)(a1 + 16) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a1 + 16));
        v_stack_p8 = (unsigned int)(result);
    }
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpApicEndOfInterruptReadIoApicIndex(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) goto loc_00569AB9;
    result = *(uint64_t *)(Arg1 + 0x10);
    if (*(uint64_t *)(Arg1 + 0x10) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(Arg1 + 0x10));
        v_stack_p8 = (uint32_t)(result);
    }
    result = guard_dispatch_icall(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00569AA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00569AA0[BB_00569AA0]
  bb_00569AA9[BB_00569AA9]
  bb_00569AB2[BB_00569AB2]
  bb_00569AB9[BB_00569AB9]
  bb_00569ACA[BB_00569ACA]
  bb_00569AA0 -->|branch| bb_00569AB9
  bb_00569AA0 -->|fallthrough| bb_00569AA9
  bb_00569AA9 -->|branch| bb_00569AB9
  bb_00569AA9 -->|fallthrough| bb_00569AB2
  bb_00569AB2 -->|flow| bb_00569AB9
```
