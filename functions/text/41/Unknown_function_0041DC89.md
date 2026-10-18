# sub_0041DC89

- RVA: `0x0041DC89`–`0x0041DCBB` (길이 `50` bytes)
- VA: `0x000000014041DC89`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009F914`
- 디코드: `15`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0041DC9C` → [sub_0041DCBB + 0xE](Unknown_function_0041DCBB.md) (`tail-transfer`)
  - `0x0041DCA9` → [sub_0041DCBB](Unknown_function_0041DCBB.md) (`tail-transfer`)
  - `0x0041DCB6` → [RtlAreBitsClearEx + 0x35](RtlAreBitsClearEx_function_0041DBF0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0041DC89  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
0041DC90  48 8B CA                        mov rcx, rdx
0041DC93  49 8B C0                        mov rax, r8
0041DC96  48 D3 E0                        shl rax, cl
0041DC99  48 85 D8                        test rax, rbx
0041DC9C  75 2B                           jne 0x14041dcc9
0041DC9E  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0041DCA2  49 83 C1 08                     add r9, 8
0041DCA6  4D 3B CA                        cmp r9, r10
0041DCA9  74 10                           je 0x14041dcbb
0041DCAB  48 85 C0                        test rax, rax
0041DCAE  74 EE                           je 0x14041dc9e
0041DCB0  48 8B 1C 24                     mov rbx, qword ptr [rsp]
0041DCB4  32 C0                           xor al, al
0041DCB6  E9 6A FF FF FF                  jmp 0x14041dc25
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0041DC89(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    unsigned __int64 v_stack_p0;

    result = (-1) << ((unsigned __int8)(a2));
loc_0041DC9E:
    a4 = (a4) + (8);
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_0041DC9E;
    result = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0041DC89(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    uint64_t v_stack_p0;

    result = (-1) << ((uint8_t)(Arg2));
loc_0041DC9E:
    Arg4 = (Arg4) + (8);
    if (*(uint64_t *)(Arg4 + 0x8) == 0) goto loc_0041DC9E;
    result = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041DC89&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041DC89[BB_0041DC89]
  bb_0041DC9E[BB_0041DC9E]
  bb_0041DCAB[BB_0041DCAB]
  bb_0041DCB0[BB_0041DCB0]
  bb_0041DC89 -->|fallthrough| bb_0041DC9E
  bb_0041DC9E -->|fallthrough| bb_0041DCAB
  bb_0041DCAB -->|branch| bb_0041DC9E
  bb_0041DCAB -->|fallthrough| bb_0041DCB0
```
