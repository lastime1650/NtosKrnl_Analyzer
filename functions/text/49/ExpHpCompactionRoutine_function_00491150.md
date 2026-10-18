# ExpHpCompactionRoutine

- RVA: `0x00491150`–`0x0049118E` (길이 `62` bytes)
- VA: `0x0000000140491150`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE6C`
- 디코드: `16`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00491160` → [ExpHpEnumerateHeaps](ExpHpEnumerateHeaps_function_00491194.md) (function, `0x00491194`)
- `0x00491167` → [ExpCompactPrivatePools](../../page/A5/ExpCompactPrivatePools_function_00A5FD08.md) (function, `0x00A5FD08`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00491156` → RVA `0x002E75F0` (`ExpHpCompactHeapCallback`; read)
- `0x00491171` → RVA `0x00EFA7C0` (`.data`; write)
- `0x00491182` → RVA `0x00EFA7BC` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00491167` → [ExpCompactPrivatePools](../../page/A5/ExpCompactPrivatePools_function_00A5FD08.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00491150  40 53                           push rbx
00491152  48 83 EC 20                     sub rsp, 0x20
00491156  48 8D 15 93 64 E5 FF            lea rdx, [rip - 0x1a9b6d]
0049115D  48 8B D9                        mov rbx, rcx
00491160  E8 2F 00 00 00                  call 0x140491194
00491165  8B CB                           mov ecx, ebx
00491167  E8 9C EB 5C 00                  call 0x140a5fd08
0049116C  83 FB 01                        cmp ebx, 1
0049116F  74 11                           je 0x140491182
00491171  C7 05 45 96 A6 00 00 00 00 00   mov dword ptr [rip + 0xa69645], 0
0049117B  48 83 C4 20                     add rsp, 0x20
0049117F  5B                              pop rbx
00491180  C3                              ret
00491181  CC                              int3
00491182  C7 05 30 96 A6 00 00 00 00 00   mov dword ptr [rip + 0xa69630], 0
0049118C  EB ED                           jmp 0x14049117b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpHpCompactionRoutine(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExpHpEnumerateHeaps(a1, v_rip - 1743725, a3, a4);
    result = ExpCompactPrivatePools((unsigned int)((unsigned int)(a1)), v_rip - 1743725, a3, a4);
    if (((unsigned int)(a1)) == 1) goto loc_00491182;
    *(unsigned int *)(v_rip + 10917445) = 0;
loc_0049117B:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00491182:
    *(unsigned int *)(v_rip + 10917424) = 0;
    goto loc_0049117B;
}
```

## 5. (Beta) C Style

```c
int64_t ExpHpCompactionRoutine(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExpHpEnumerateHeaps(Arg1, v_rip - 1743725, a3, a4);
    result = ExpCompactPrivatePools((uint32_t)((uint32_t)(Arg1)), v_rip - 1743725, a3, a4);
    if (((uint32_t)(Arg1)) == 1) goto loc_00491182;
    *(uint32_t *)(v_rip + 0xA69645) = 0;
loc_0049117B:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00491182:
    *(uint32_t *)(v_rip + 0xA69630) = 0;
    goto loc_0049117B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00491150&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00491150[BB_00491150]
  bb_00491171[BB_00491171]
  bb_0049117B[BB_0049117B]
  bb_00491181[BB_00491181]
  bb_00491182[BB_00491182]
  bb_00491150 -->|branch| bb_00491182
  bb_00491150 -->|fallthrough| bb_00491171
  bb_00491171 -->|flow| bb_0049117B
  bb_00491181 -->|flow| bb_00491182
  bb_00491182 -->|branch| bb_0049117B
```
