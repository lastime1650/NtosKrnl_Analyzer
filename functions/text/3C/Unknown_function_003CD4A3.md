# sub_003CD4A3

- RVA: `0x003CD4A3`–`0x003CD4DB` (길이 `56` bytes)
- VA: `0x00000001403CD4A3`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008F9C4`
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
- `0x003CD4C5` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003CD4CF` → [sub_003CD4EA](Unknown_function_003CD4EA.md) (`tail-transfer`)
  - `0x003CD4D9` → [sub_003CD4DB + 0x5](Unknown_function_003CD4DB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003CD4A3  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
003CD4A8  48 8B EB                        mov rbp, rbx
003CD4AB  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
003CD4B0  48 BE 00 00 00 00 00 80 00 00   movabs rsi, 0x800000000000
003CD4BA  48 03 F1                        add rsi, rcx
003CD4BD  48 C1 ED 03                     shr rbp, 3
003CD4C1  48 C1 EE 03                     shr rsi, 3
003CD4C5  48 03 35 0C 9A BF 00            add rsi, qword ptr [rip + 0xbf9a0c]
003CD4CC  48 85 ED                        test rbp, rbp
003CD4CF  75 19                           jne 0x1403cd4ea
003CD4D1  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
003CD4D6  F6 C3 07                        test bl, 7
003CD4D9  74 05                           je 0x1403cd4e0
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_003CD4A3(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
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
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip + 12556812));
}
```

## 5. (Beta) C Style

```c
void sub_003CD4A3(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
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
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip + 0xBF9A0C));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CD4A3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003CD4A3[BB_003CD4A3]
  bb_003CD4D1[BB_003CD4D1]
  bb_003CD4A3 -->|fallthrough| bb_003CD4D1
```
