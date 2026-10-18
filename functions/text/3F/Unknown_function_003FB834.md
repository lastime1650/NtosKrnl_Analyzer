# sub_003FB834

- RVA: `0x003FB834`–`0x003FB86C` (길이 `56` bytes)
- VA: `0x00000001403FB834`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00098600`
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
- `0x003FB856` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003FB860` → [sub_003FB87B](Unknown_function_003FB87B.md) (`tail-transfer`)
  - `0x003FB86A` → [sub_003FB86C + 0x5](Unknown_function_003FB86C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FB834  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
003FB839  48 8B EB                        mov rbp, rbx
003FB83C  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
003FB841  48 BE 00 00 00 00 00 80 00 00   movabs rsi, 0x800000000000
003FB84B  48 03 F1                        add rsi, rcx
003FB84E  48 C1 ED 03                     shr rbp, 3
003FB852  48 C1 EE 03                     shr rsi, 3
003FB856  48 03 35 7B B6 BC 00            add rsi, qword ptr [rip + 0xbcb67b]
003FB85D  48 85 ED                        test rbp, rbp
003FB860  75 19                           jne 0x1403fb87b
003FB862  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
003FB867  F6 C3 07                        test bl, 7
003FB86A  74 05                           je 0x1403fb871
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_003FB834(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
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
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip + 12367483));
}
```

## 5. (Beta) C Style

```c
void sub_003FB834(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
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
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip + 0xBCB67B));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FB834&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FB834[BB_003FB834]
  bb_003FB862[BB_003FB862]
  bb_003FB834 -->|fallthrough| bb_003FB862
```
