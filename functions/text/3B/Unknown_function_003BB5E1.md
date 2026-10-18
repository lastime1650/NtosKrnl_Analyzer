# sub_003BB5E1

- RVA: `0x003BB5E1`–`0x003BB605` (길이 `36` bytes)
- VA: `0x00000001403BB5E1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008CC58`
- 디코드: `11`개 명령, `36/36` bytes 표시
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
  - `0x003BB5E8` → [sub_003BB6B7](Unknown_function_003BB6B7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003BB5E1  48 81 FF 9F 00 00 00            cmp rdi, 0x9f
003BB5E8  0F 82 C9 00 00 00               jb 0x1403bb6b7
003BB5EE  41 8B C7                        mov eax, r15d
003BB5F1  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
003BB5F6  48 8B 6C 24 50                  mov rbp, qword ptr [rsp + 0x50]
003BB5FB  48 83 C4 20                     add rsp, 0x20
003BB5FF  41 5F                           pop r15
003BB601  5F                              pop rdi
003BB602  5E                              pop rsi
003BB603  C3                              ret
003BB604  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003BB5E1(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_r15));
}
```

## 5. (Beta) C Style

```c
int64_t sub_003BB5E1(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9, int64_t Arg10)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_r15));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BB5E1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003BB5E1[BB_003BB5E1]
  bb_003BB5EE[BB_003BB5EE]
  bb_003BB604[BB_003BB604]
  bb_003BB5E1 -->|fallthrough| bb_003BB5EE
```
