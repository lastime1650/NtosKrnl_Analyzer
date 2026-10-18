# sub_002F016E

- RVA: `0x002F016E`–`0x002F0187` (길이 `25` bytes)
- VA: `0x00000001402F016E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071BB8`
- 디코드: `9`개 명령, `25/25` bytes 표시
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
  - `0x002F0176` → [sub_002F01AB](Unknown_function_002F01AB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F016E  48 83 E3 F0                     and rbx, 0xfffffffffffffff0
002F0172  48 83 F8 01                     cmp rax, 1
002F0176  74 33                           je 0x1402f01ab
002F0178  48 8B C3                        mov rax, rbx
002F017B  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
002F0180  48 83 C4 20                     add rsp, 0x20
002F0184  5F                              pop rdi
002F0185  C3                              ret
002F0186  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002F016E(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 v_rbx;
    __int64 v_rsp;

    v_rbx = (v_rbx) & (-16);
    v_rsp = (v_rsp) + (32);
    return v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002F016E(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, int64_t Arg7)
{
    int64_t local_rbx;
    int64_t local_rsp;

    local_rbx = (local_rbx) & (-16);
    local_rsp = (local_rsp) + (32);
    return local_rbx;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F016E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F016E[BB_002F016E]
  bb_002F0178[BB_002F0178]
  bb_002F0186[BB_002F0186]
  bb_002F016E -->|fallthrough| bb_002F0178
```
