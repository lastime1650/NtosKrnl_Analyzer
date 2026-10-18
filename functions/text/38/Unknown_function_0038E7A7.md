# sub_0038E7A7

- RVA: `0x0038E7A7`–`0x0038E7DF` (길이 `56` bytes)
- VA: `0x000000014038E7A7`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00080654`
- 디코드: `13`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0038E7C9` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0038E7D3` → [sub_0038E7EE](Unknown_function_0038E7EE.md) (`tail-transfer`)
  - `0x0038E7DD` → [sub_0038E7DF + 0x5](Unknown_function_0038E7DF.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0038E7A7  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
0038E7AC  48 8B EB                        mov rbp, rbx
0038E7AF  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0038E7B4  48 BE 00 00 00 00 00 80 00 00   movabs rsi, 0x800000000000
0038E7BE  48 03 F1                        add rsi, rcx
0038E7C1  48 C1 ED 03                     shr rbp, 3
0038E7C5  48 C1 EE 03                     shr rsi, 3
0038E7C9  48 03 35 08 87 C3 00            add rsi, qword ptr [rip + 0xc38708]
0038E7D0  48 85 ED                        test rbp, rbp
0038E7D3  75 19                           jne 0x14038e7ee
0038E7D5  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
0038E7DA  F6 C3 07                        test bl, 7
0038E7DD  74 05                           je 0x14038e7e4
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0038E7A7(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 v_rbp;
    __int64 v_rsi;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;

    v_stack_p40 = v_rbp;
    v_stack_p48 = v_rsi;
    v_rsi = (v_rsi) + (a1);
    v_rbp = (v_rbx) >> (3);
    v_rsi = (v_rsi) >> (3);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip + 12814088));
}
```

## 5. (Beta) C Style

```c
void sub_0038E7A7(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
{
    int64_t local_rbp;
    int64_t local_rsi;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;

    v_stack_p40 = local_rbp;
    v_stack_p48 = local_rsi;
    local_rsi = (local_rsi) + (Arg1);
    local_rbp = (local_rbx) >> (3);
    local_rsi = (local_rsi) >> (3);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip + 0xC38708));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038E7A7&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038E7A7[BB_0038E7A7]
  bb_0038E7D5[BB_0038E7D5]
  bb_0038E7A7 -->|fallthrough| bb_0038E7D5
```
