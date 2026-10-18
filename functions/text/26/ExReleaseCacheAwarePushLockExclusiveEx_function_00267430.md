# ExReleaseCacheAwarePushLockExclusiveEx

- RVA: `0x00267430`–`0x00267447` (길이 `23` bytes)
- VA: `0x0000000140267430`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064FA4`
- 디코드: `7`개 명령, `23/23` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00267445` → [sub_002674A9](Unknown_function_002674A9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00267430  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00267435  56                              push rsi
00267436  48 83 EC 30                     sub rsp, 0x30
0026743A  8B EA                           mov ebp, edx
0026743C  48 8B F1                        mov rsi, rcx
0026743F  F7 C2 F8 FF FF FF               test edx, 0xfffffff8
00267445  75 62                           jne 0x1402674a9
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall ExReleaseCacheAwarePushLockExclusiveEx(__int64 a1, int a2)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (48);
}
```

## 5. (Beta) C Style

```c
void ExReleaseCacheAwarePushLockExclusiveEx(int64_t Arg1, int32_t Arg2)
{
    int64_t local_rsp;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (48);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00267430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00267430[BB_00267430]
```
