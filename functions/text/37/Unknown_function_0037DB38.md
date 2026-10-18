# sub_0037DB38

- RVA: `0x0037DB38`–`0x0037DB53` (길이 `27` bytes)
- VA: `0x000000014037DB38`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B514`
- 디코드: `7`개 명령, `27/27` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0037DB38  48 89 6C 24 70                  mov qword ptr [rsp + 0x70], rbp
0037DB3D  45 0F B6 E8                     movzx r13d, r8b
0037DB41  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0037DB46  48 8B D9                        mov rbx, rcx
0037DB49  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0037DB4E  48 8B F2                        mov rsi, rdx
0037DB51  33 FF                           xor edi, edi
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0037DB38(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 v_rdi;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p70;

    v_stack_p70 = v_rbp;
    v_stack_p40 = v_rsi;
    v_stack_p38 = v_rdi;
    v_rdi = 0;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_0037DB38(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t local_rdi;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p70;

    v_stack_p70 = local_rbp;
    v_stack_p40 = local_rsi;
    v_stack_p38 = local_rdi;
    local_rdi = 0;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037DB38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0037DB38[BB_0037DB38]
```
