# sub_0086FD23

- RVA: `0x0086FD23`–`0x0086FD40` (길이 `29` bytes)
- VA: `0x000000014086FD23`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C220`
- 디코드: `10`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0086FD23` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0086FD23` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0086FD23  E8 58 60 C0 FF                  call 0x140475d80
0086FD28  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
0086FD2B  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0086FD2F  89 01                           mov dword ptr [rcx], eax
0086FD31  40 0F B6 C6                     movzx eax, sil
0086FD35  48 81 C4 B8 00 00 00            add rsp, 0xb8
0086FD3C  5E                              pop rsi
0086FD3D  5D                              pop rbp
0086FD3E  C3                              ret
0086FD3F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0086FD23(void)
{
    __int64 result;
    __int64 v_rsp;

    result = CmSiFreeMemory(a1, a2, a3, a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 127)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 33)));
    v_rsp = (v_rsp) + (184);
    return (unsigned __int8)(v_rsi);
}
```

## 5. (Beta) C Style

```c
void sub_0086FD23(void)
{
    int64_t result;
    int64_t local_rsp;

    result = CmSiFreeMemory(a1, a2, a3, a4);
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x7F)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x21)));
    local_rsp = (local_rsp) + (184);
    return (uint8_t)(local_rsi);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086FD23&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0086FD23[BB_0086FD23]
  bb_0086FD3F[BB_0086FD3F]
```
