# sub_0099DCFA

- RVA: `0x0099DCFA`–`0x0099DD1B` (길이 `33` bytes)
- VA: `0x000000014099DCFA`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A144`
- 디코드: `12`개 명령, `33/33` bytes 표시
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
  - `0x0099DD01` → [sub_0099DD56](Unknown_function_0099DD56.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0099DCFA  48 8B 5D 58                     mov rbx, qword ptr [rbp + 0x58]
0099DCFE  4D 85 F6                        test r14, r14
0099DD01  75 53                           jne 0x14099dd56
0099DD03  48 8D 43 20                     lea rax, [rbx + 0x20]
0099DD07  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0099DD0C  48 8B 6C 24 50                  mov rbp, qword ptr [rsp + 0x50]
0099DD11  48 83 C4 20                     add rsp, 0x20
0099DD15  41 5E                           pop r14
0099DD17  5F                              pop rdi
0099DD18  5E                              pop rsi
0099DD19  C3                              ret
0099DD1A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0099DCFA(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(v_rbp + 88) + 32;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0099DCFA(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9, int64_t Arg10)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(local_rbp + 0x58) + 32;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099DCFA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0099DCFA[BB_0099DCFA]
  bb_0099DD03[BB_0099DD03]
  bb_0099DD1A[BB_0099DD1A]
  bb_0099DCFA -->|fallthrough| bb_0099DD03
```
