# ExpTimeZoneDpcRoutine$fin$0

- RVA: `0x006D5C46`–`0x006D5C9D` (길이 `87` bytes)
- VA: `0x00000001406D5C46`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF4C0`
- 디코드: `27`개 명령, `87/87` bytes 표시
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
006D5C46  40 55                           push rbp
006D5C48  48 83 EC 30                     sub rsp, 0x30
006D5C4C  48 8B EA                        mov rbp, rdx
006D5C4F  88 4D 48                        mov byte ptr [rbp + 0x48], cl
006D5C52  84 C9                           test cl, cl
006D5C54  74 40                           je 0x1406d5c96
006D5C56  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D5C59  83 F8 08                        cmp eax, 8
006D5C5C  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D5C5F  75 2F                           jne 0x1406d5c90
006D5C61  83 C0 08                        add eax, 8
006D5C64  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D5C67  48 8D 85 E9 00 00 00            lea rax, [rbp + 0xe9]
006D5C6E  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
006D5C72  48 83 65 68 00                  and qword ptr [rbp + 0x68], 0
006D5C77  48 8B 8D E9 00 00 00            mov rcx, qword ptr [rbp + 0xe9]
006D5C7E  48 89 4D 68                     mov qword ptr [rbp + 0x68], rcx
006D5C82  48 8B 85 D9 00 00 00            mov rax, qword ptr [rbp + 0xd9]
006D5C89  48 D3 C8                        ror rax, cl
006D5C8C  8B 00                           mov eax, dword ptr [rax]
006D5C8E  EB 06                           jmp 0x1406d5c96
006D5C90  83 C0 0B                        add eax, 0xb
006D5C93  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D5C96  48 83 C4 30                     add rsp, 0x30
006D5C9A  5D                              pop rbp
006D5C9B  C3                              ret
006D5C9C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTimeZoneDpcRoutine_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int8 *)(a2 + 72) = a1;
    if (a1 == 0) goto loc_006D5C96;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) != 8) goto loc_006D5C90;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 48))) + (8));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
    *(unsigned __int64 *)(a2 + 88) = a2 + 233;
    *(unsigned __int64 *)(a2 + 104) = *(unsigned __int64 *)(a2 + 233);
    goto loc_006D5C96;
loc_006D5C90:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 217)))) + (11));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
loc_006D5C96:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpTimeZoneDpcRoutine_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    *(uint8_t *)(arg2 + 0x48) = Arg1;
    if (Arg1 == 0) goto loc_006D5C96;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) != 8) goto loc_006D5C90;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x30))) + (8));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
    *(void **)(arg2 + 0x58) = Arg2 + 233;
    *(uint64_t *)(arg2 + 0x68) = *(uint64_t *)(arg2 + 0xE9);
    goto loc_006D5C96;
loc_006D5C90:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xD9)))) + (11));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
loc_006D5C96:
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x48` | `8` | `W` |
| `Arg2` | `+ 0x58` | `64` | `W` |
| `Arg2` | `+ 0x68` | `64` | `R/W` |
| `Arg2` | `+ 0x68` | `64` | `W` |
| `Arg2` | `+ 0xD9` | `64` | `R` |
| `Arg2` | `+ 0xE9` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D5C46&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D5C46[BB_006D5C46]
  bb_006D5C56[BB_006D5C56]
  bb_006D5C61[BB_006D5C61]
  bb_006D5C90[BB_006D5C90]
  bb_006D5C96[BB_006D5C96]
  bb_006D5C9C[BB_006D5C9C]
  bb_006D5C46 -->|branch| bb_006D5C96
  bb_006D5C46 -->|fallthrough| bb_006D5C56
  bb_006D5C56 -->|branch| bb_006D5C90
  bb_006D5C56 -->|fallthrough| bb_006D5C61
  bb_006D5C61 -->|branch| bb_006D5C96
  bb_006D5C90 -->|flow| bb_006D5C96
```
