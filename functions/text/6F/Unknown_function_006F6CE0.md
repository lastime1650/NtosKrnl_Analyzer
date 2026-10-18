# sub_006F6CE0

- RVA: `0x006F6CE0`–`0x006F6D7D` (길이 `157` bytes)
- VA: `0x00000001406F6CE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B29B4`
- 디코드: `38`개 명령, `157/157` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006F6D72` → [tlgWriteEx_EtwWriteEx](../4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006F6D0F` → RVA `0x00059AEB` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F6D78` → [MiStoreLogWriteIssueFailure + 0x42](../48/MiStoreLogWriteIssueFailure_function_0048EE4C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F6CE0  83 65 03 00                     and dword ptr [rbp + 3], 0
006F6CE4  48 8D 45 B7                     lea rax, [rbp - 0x49]
006F6CE8  83 65 13 00                     and dword ptr [rbp + 0x13], 0
006F6CEC  83 65 23 00                     and dword ptr [rbp + 0x23], 0
006F6CF0  83 65 33 00                     and dword ptr [rbp + 0x33], 0
006F6CF4  83 65 43 00                     and dword ptr [rbp + 0x43], 0
006F6CF8  48 89 45 F7                     mov qword ptr [rbp - 9], rax
006F6CFC  48 8B 02                        mov rax, qword ptr [rdx]
006F6CFF  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
006F6D03  48 8D 45 C7                     lea rax, [rbp - 0x39]
006F6D07  48 89 45 07                     mov qword ptr [rbp + 7], rax
006F6D0B  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
006F6D0F  48 8D 15 D5 2D 96 FF            lea rdx, [rip - 0x69d22b]
006F6D16  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
006F6D1A  48 8D 45 CF                     lea rax, [rbp - 0x31]
006F6D1E  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
006F6D22  48 8D 45 BB                     lea rax, [rbp - 0x45]
006F6D26  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
006F6D2A  48 8D 45 BF                     lea rax, [rbp - 0x41]
006F6D2E  44 89 5D B7                     mov dword ptr [rbp - 0x49], r11d
006F6D32  41 BB 04 00 00 00               mov r11d, 4
006F6D38  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
006F6D3C  48 8D 45 D7                     lea rax, [rbp - 0x29]
006F6D40  44 89 4D BF                     mov dword ptr [rbp - 0x41], r9d
006F6D44  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
006F6D49  41 8D 4B 04                     lea ecx, [r11 + 4]
006F6D4D  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
006F6D55  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
006F6D58  45 8D 4B FD                     lea r9d, [r11 - 3]
006F6D5C  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
006F6D5F  49 8B CA                        mov rcx, r10
006F6D62  44 89 5D FF                     mov dword ptr [rbp - 1], r11d
006F6D66  44 89 45 BB                     mov dword ptr [rbp - 0x45], r8d
006F6D6A  44 89 5D 2F                     mov dword ptr [rbp + 0x2f], r11d
006F6D6E  44 89 5D 3F                     mov dword ptr [rbp + 0x3f], r11d
006F6D72  E8 D1 35 DB FF                  call 0x1404aa348
006F6D77  90                              nop
006F6D78  E9 11 81 D9 FF                  jmp 0x14048ee8e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F6CE0(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;

    *(unsigned __int64 *)(v_rbp - 9) = v_rbp - 73;
    *(unsigned __int64 *)(v_rbp - 57) = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(v_rbp + 7) = v_rbp - 57;
    *(unsigned __int64 *)(v_rbp - 49) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned __int64 *)(v_rbp + 23) = v_rbp - 49;
    *(unsigned __int64 *)(v_rbp + 39) = v_rbp - 69;
    *(unsigned int *)(v_rbp - 73) = (unsigned int)(v_r11);
    *(unsigned __int64 *)(v_rbp + 55) = v_rbp - 65;
    *(unsigned int *)(v_rbp - 65) = a4;
    v_stack_p38 = v_rbp - 41;
    v_stack_p30 = 7;
    *(unsigned int *)(v_rbp + 15) = (unsigned int)(4 + 4);
    *(unsigned int *)(v_rbp + 31) = (unsigned int)(4 + 4);
    *(unsigned int *)(v_rbp - 1) = 4;
    *(unsigned int *)(v_rbp - 69) = a3;
    *(unsigned int *)(v_rbp + 47) = 4;
    *(unsigned int *)(v_rbp + 63) = 4;
    result = tlgWriteEx_EtwWriteEx(v_r10, v_rip - 6935083, a3, 4 - 3);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F6CE0(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;

    *(uint64_t *)(local_rbp - 0x9) = local_rbp - 73;
    *(uint64_t *)(local_rbp - 0x39) = *(uint64_t *)(arg2);
    *(uint64_t *)(local_rbp + 0x7) = local_rbp - 57;
    *(uint64_t *)(local_rbp - 0x31) = *(uint64_t *)(arg2 + 0x8);
    *(uint64_t *)(local_rbp + 0x17) = local_rbp - 49;
    *(uint64_t *)(local_rbp + 0x27) = local_rbp - 69;
    *(uint32_t *)(local_rbp - 0x49) = (uint32_t)(local_r11);
    *(uint64_t *)(local_rbp + 0x37) = local_rbp - 65;
    *(uint32_t *)(local_rbp - 0x41) = Arg4;
    v_stack_p38 = local_rbp - 41;
    v_stack_p30 = 7;
    *(uint32_t *)(local_rbp + 0xF) = (uint32_t)(4 + 4);
    *(uint32_t *)(local_rbp + 0x1F) = (uint32_t)(4 + 4);
    *(uint32_t *)(local_rbp - 0x1) = 4;
    *(uint32_t *)(local_rbp - 0x45) = Arg3;
    *(uint32_t *)(local_rbp + 0x2F) = 4;
    *(uint32_t *)(local_rbp + 0x3F) = 4;
    result = tlgWriteEx_EtwWriteEx(local_r10, v_rip - 6935083, Arg3, 4 - 3);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F6CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F6CE0[BB_006F6CE0]
```
