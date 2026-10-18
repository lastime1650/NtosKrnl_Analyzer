# sub_002B7857

- RVA: `0x002B7857`–`0x002B78A5` (길이 `78` bytes)
- VA: `0x00000001402B7857`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006DA60`
- 디코드: `20`개 명령, `78/78` bytes 표시
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
  - `0x002B789F` → [sub_002B79A7](Unknown_function_002B79A7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B7857  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
002B785C  48 8B F9                        mov rdi, rcx
002B785F  8B 71 30                        mov esi, dword ptr [rcx + 0x30]
002B7862  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
002B7867  4C 8B EA                        mov r13, rdx
002B786A  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
002B786F  4D 8B F8                        mov r15, r8
002B7872  44 8B 41 20                     mov r8d, dword ptr [rcx + 0x20]
002B7876  C1 EE 12                        shr esi, 0x12
002B7879  83 E6 03                        and esi, 3
002B787C  4B 8D 1C 7F                     lea rbx, [r15 + r15*2]
002B7880  48 C1 E3 04                     shl rbx, 4
002B7884  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B788E  48 03 D8                        add rbx, rax
002B7891  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
002B7894  C1 E8 10                        shr eax, 0x10
002B7897  0F B6 C8                        movzx ecx, al
002B789A  C1 E9 06                        shr ecx, 6
002B789D  3B CE                           cmp ecx, esi
002B789F  0F 85 02 01 00 00               jne 0x1402b79a7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002B7857(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p58;

    v_stack_p58 = v_rsi;
    v_stack_p30 = v_r13;
    v_stack_p20 = v_r15;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) >> (18));
    v_rsi = (unsigned int)((v_rsi) & (3));
    v_rbx = (a3 + a3 * 2) << (4);
    v_rbx = (v_rbx) + (result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
}
```

## 5. (Beta) C Style

```c
int64_t sub_002B7857(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p58;

    v_stack_p58 = local_rsi;
    v_stack_p30 = local_r13;
    v_stack_p20 = local_r15;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (18));
    local_rsi = (uint32_t)((local_rsi) & (3));
    local_rbx = (Arg3 + Arg3 * 2) << (4);
    local_rbx = (local_rbx) + (result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg3` | `+ 0x0 + r15*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B7857&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002B7857[BB_002B7857]
```
