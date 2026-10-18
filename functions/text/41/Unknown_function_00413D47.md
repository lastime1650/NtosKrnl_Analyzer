# sub_00413D47

- RVA: `0x00413D47`–`0x00413D79` (길이 `50` bytes)
- VA: `0x0000000140413D47`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BFFC`
- 디코드: `11`개 명령, `50/50` bytes 표시
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
00413D47  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00413D4C  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
00413D51  48 8B 75 68                     mov rsi, qword ptr [rbp + 0x68]
00413D55  48 2B 75 28                     sub rsi, qword ptr [rbp + 0x28]
00413D59  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00413D5E  48 8B CE                        mov rcx, rsi
00413D61  48 8B BD 98 00 00 00            mov rdi, qword ptr [rbp + 0x98]
00413D68  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00413D6D  4C 8B 65 60                     mov r12, qword ptr [rbp + 0x60]
00413D71  4C 2B 65 20                     sub r12, qword ptr [rbp + 0x20]
00413D75  4C 8B 4F 08                     mov r9, qword ptr [rdi + 8]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00413D47(void)
{
    __int64 v_r12;
    __int64 v_rsi;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;

    v_stack_p70 = v_rbx;
    v_stack_p68 = v_rsi;
    v_rsi = (*(unsigned __int64 *)(v_rbp + 104)) - (*(unsigned __int64 *)(v_rbp + 40));
    v_stack_p60 = v_rdi;
    v_stack_p58 = v_r12;
    v_r12 = (*(unsigned __int64 *)(v_rbp + 96)) - (*(unsigned __int64 *)(v_rbp + 32));
    return;
}
```

## 5. (Beta) C Style

```c
void sub_00413D47(void)
{
    int64_t local_r12;
    int64_t local_rsi;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;

    v_stack_p70 = local_rbx;
    v_stack_p68 = local_rsi;
    local_rsi = (*(uint64_t *)(local_rbp + 0x68)) - (*(uint64_t *)(local_rbp + 0x28));
    v_stack_p60 = local_rdi;
    v_stack_p58 = local_r12;
    local_r12 = (*(uint64_t *)(local_rbp + 0x60)) - (*(uint64_t *)(local_rbp + 0x20));
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00413D47&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00413D47[BB_00413D47]
```
