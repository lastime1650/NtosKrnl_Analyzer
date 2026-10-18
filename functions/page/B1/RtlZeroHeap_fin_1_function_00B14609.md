# RtlZeroHeap$fin$1

- RVA: `0x00B14609`–`0x00B1465F` (길이 `86` bytes)
- VA: `0x0000000140B14609`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000CFB78`
- 디코드: `29`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B14651` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B14651` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B14609  40 55                           push rbp
00B1460B  57                              push rdi
00B1460C  48 83 EC 38                     sub rsp, 0x38
00B14610  48 8B EA                        mov rbp, rdx
00B14613  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
00B14617  48 85 D2                        test rdx, rdx
00B1461A  74 24                           je 0x140b14640
00B1461C  48 8B 7D 50                     mov rdi, qword ptr [rbp + 0x50]
00B14620  83 7F 7C 00                     cmp dword ptr [rdi + 0x7c], 0
00B14624  74 1A                           je 0x140b14640
00B14626  8A 4A 0A                        mov cl, byte ptr [rdx + 0xa]
00B14629  32 4A 09                        xor cl, byte ptr [rdx + 9]
00B1462C  32 4A 08                        xor cl, byte ptr [rdx + 8]
00B1462F  88 4A 0B                        mov byte ptr [rdx + 0xb], cl
00B14632  8B 42 08                        mov eax, dword ptr [rdx + 8]
00B14635  8B 8F 88 00 00 00               mov ecx, dword ptr [rdi + 0x88]
00B1463B  33 C8                           xor ecx, eax
00B1463D  89 4A 08                        mov dword ptr [rdx + 8], ecx
00B14640  80 7D 30 00                     cmp byte ptr [rbp + 0x30], 0
00B14644  74 11                           je 0x140b14657
00B14646  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00B1464A  48 8B 89 60 01 00 00            mov rcx, qword ptr [rcx + 0x160]
00B14651  E8 BA B3 74 FF                  call 0x14025fa10
00B14656  90                              nop
00B14657  48 83 C4 38                     add rsp, 0x38
00B1465B  5F                              pop rdi
00B1465C  5D                              pop rbp
00B1465D  C3                              ret
00B1465E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlZeroHeap_fin_1(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    if (*(unsigned __int64 *)(a2 + 64) == 0) goto loc_00B14640;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 80) + 124)) != 0) {
        a1 = *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 64) + 10);
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 64) + 9)));
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 64) + 8)));
        *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 64) + 11) = (unsigned __int8)(a1);
        result = *(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 8);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a2 + 80) + 136);
        a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
        *(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 8) = (unsigned int)(a1);
    }
    if ((*(unsigned __int8 *)(a2 + 48)) != 0) {
        a1 = *(unsigned __int64 *)(a2 + 80);
        a1 = *(unsigned __int64 *)(a1 + 352);
        result = ExReleaseResourceLite(a1, *(unsigned __int64 *)(a2 + 64), a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlZeroHeap_fin_1(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    if (*(uint64_t *)(arg2 + 0x40) == 0) goto loc_00B14640;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x50) + 0x7C)) != 0) {
        Arg1 = *(uint8_t *)(*(uint64_t *)(arg2 + 0x40) + 0xA);
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(*(uint64_t *)(arg2 + 0x40) + 0x9)));
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(*(uint64_t *)(arg2 + 0x40) + 0x8)));
        *(uint8_t *)(*(uint64_t *)(arg2 + 0x40) + 0xB) = (uint8_t)(Arg1);
        result = *(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x8);
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg2 + 0x50) + 0x88);
        Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
        *(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x8) = (uint32_t)(Arg1);
    }
    if ((*(uint8_t *)(arg2 + 0x30)) != 0) {
        Arg1 = *(uint64_t *)(arg2 + 0x50);
        Arg1 = *(uint64_t *)(Arg1 + 0x160);
        result = ExReleaseResourceLite(Arg1, *(uint64_t *)(arg2 + 0x40), a3, a4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `8` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B14609&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B14609[BB_00B14609]
  bb_00B1461C[BB_00B1461C]
  bb_00B14626[BB_00B14626]
  bb_00B14640[BB_00B14640]
  bb_00B14646[BB_00B14646]
  bb_00B14657[BB_00B14657]
  bb_00B1465E[BB_00B1465E]
  bb_00B14609 -->|branch| bb_00B14640
  bb_00B14609 -->|fallthrough| bb_00B1461C
  bb_00B1461C -->|branch| bb_00B14640
  bb_00B1461C -->|fallthrough| bb_00B14626
  bb_00B14626 -->|flow| bb_00B14640
  bb_00B14640 -->|branch| bb_00B14657
  bb_00B14640 -->|fallthrough| bb_00B14646
  bb_00B14646 -->|flow| bb_00B14657
```
