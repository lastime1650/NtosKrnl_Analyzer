# ExpTimeRefreshDpcRoutine$fin$2

- RVA: `0x006D4A7A`–`0x006D4AD8` (길이 `94` bytes)
- VA: `0x00000001406D4A7A`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BB128`
- 디코드: `26`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006D4AA9` → [local_unwind](../4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006D4A9B` → RVA `0x004B8EAA` (`.text`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D4A7A  40 55                           push rbp
006D4A7C  48 83 EC 30                     sub rsp, 0x30
006D4A80  48 8B EA                        mov rbp, rdx
006D4A83  88 4D 51                        mov byte ptr [rbp + 0x51], cl
006D4A86  84 C9                           test cl, cl
006D4A88  74 47                           je 0x1406d4ad1
006D4A8A  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D4A8D  83 F8 1C                        cmp eax, 0x1c
006D4A90  75 1D                           jne 0x1406d4aaf
006D4A92  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D4A95  83 C0 07                        add eax, 7
006D4A98  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D4A9B  48 8D 15 08 44 DE FF            lea rdx, [rip - 0x21bbf8]
006D4AA2  48 8B 8D A8 01 00 00            mov rcx, qword ptr [rbp + 0x1a8]
006D4AA9  E8 92 B0 E2 FF                  call 0x1404ffb40
006D4AAE  90                              nop
006D4AAF  48 83 A5 C8 00 00 00 00         and qword ptr [rbp + 0xc8], 0
006D4AB7  48 8B 8D 98 01 00 00            mov rcx, qword ptr [rbp + 0x198]
006D4ABE  48 89 8D C8 00 00 00            mov qword ptr [rbp + 0xc8], rcx
006D4AC5  48 8B 85 80 01 00 00            mov rax, qword ptr [rbp + 0x180]
006D4ACC  48 D3 C8                        ror rax, cl
006D4ACF  8B 00                           mov eax, dword ptr [rax]
006D4AD1  48 83 C4 30                     add rsp, 0x30
006D4AD5  5D                              pop rbp
006D4AD6  C3                              ret
006D4AD7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTimeRefreshDpcRoutine_fin_2(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int8 *)(a2 + 81) = a1;
    if (a1 == 0) goto loc_006D4AD1;
    result = (unsigned int)(*(unsigned int *)(a2 + 48));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) == 28) {
        result = *(unsigned int *)(a2 + 48);
        result = (unsigned int)((result) + (7));
        *(unsigned int *)(a2 + 48) = (unsigned int)(result);
        a2 = v_rip - 2210808;
        a1 = *(unsigned __int64 *)(a2 + 424);
        result = local_unwind(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(a2 + 200) = *(unsigned __int64 *)(a2 + 408);
loc_006D4AD1:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 384)));
}
```

## 5. (Beta) C Style

```c
int64_t ExpTimeRefreshDpcRoutine_fin_2(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    *(uint8_t *)(arg2 + 0x51) = Arg1;
    if (Arg1 == 0) goto loc_006D4AD1;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x30));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) == 28) {
        result = *(uint32_t *)(arg2 + 0x30);
        result = (uint32_t)((result) + (7));
        *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
        Arg2 = v_rip - 2210808;
        Arg1 = *(uint64_t *)(arg2 + 0x1A8);
        result = local_unwind(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(arg2 + 0xC8) = *(uint64_t *)(arg2 + 0x198);
loc_006D4AD1:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x180)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x51` | `8` | `W` |
| `Arg2` | `+ 0xC8` | `64` | `R/W` |
| `Arg2` | `+ 0xC8` | `64` | `W` |
| `Arg2` | `+ 0x180` | `64` | `R` |
| `Arg2` | `+ 0x198` | `64` | `R` |
| `Arg2` | `+ 0x1A8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D4A7A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D4A7A[BB_006D4A7A]
  bb_006D4A8A[BB_006D4A8A]
  bb_006D4A92[BB_006D4A92]
  bb_006D4AAF[BB_006D4AAF]
  bb_006D4AD1[BB_006D4AD1]
  bb_006D4AD7[BB_006D4AD7]
  bb_006D4A7A -->|branch| bb_006D4AD1
  bb_006D4A7A -->|fallthrough| bb_006D4A8A
  bb_006D4A8A -->|branch| bb_006D4AAF
  bb_006D4A8A -->|fallthrough| bb_006D4A92
  bb_006D4A92 -->|flow| bb_006D4AAF
  bb_006D4AAF -->|flow| bb_006D4AD1
```
