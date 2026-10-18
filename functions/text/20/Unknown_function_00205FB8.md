# sub_00205FB8

- RVA: `0x00205FB8`–`0x00205FE2` (길이 `42` bytes)
- VA: `0x0000000140205FB8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CE38`
- 디코드: `13`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00205FC9` → [SmKmStoreDereference](SmKmStoreDereference_function_00206574.md) (function, `0x00206574`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00205FB8  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
00205FBC  48 8B 8A 90 1D 00 00            mov rcx, qword ptr [rdx + 0x1d90]
00205FC3  8B 92 90 1A 00 00               mov edx, dword ptr [rdx + 0x1a90]
00205FC9  E8 A6 05 00 00                  call 0x140206574
00205FCE  83 FD FF                        cmp ebp, -1
00205FD1  0F 45 DD                        cmovne ebx, ebp
00205FD4  8B C3                           mov eax, ebx
00205FD6  48 81 C4 80 00 00 00            add rsp, 0x80
00205FDD  5E                              pop rsi
00205FDE  5D                              pop rbp
00205FDF  5B                              pop rbx
00205FE0  C3                              ret
00205FE1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00205FB8(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    result = SmKmStoreDereference(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + 7568), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 24) + 6800)), a3, a4);
    if (((unsigned int)(v_rbp)) != -1) { v_rbx = (unsigned int)(v_rbp); }
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
void sub_00205FB8(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    result = SmKmStoreDereference(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + 0x1D90), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x18) + 0x1A90)), a3, a4);
    if (((uint32_t)(local_rbp)) != -1) { local_rbx = (uint32_t)(local_rbp); }
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00205FB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00205FB8[BB_00205FB8]
  bb_00205FE1[BB_00205FE1]
```
