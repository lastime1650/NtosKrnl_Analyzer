# ExpTimeRefreshDpcRoutine$fin$0

- RVA: `0x006D49F6`–`0x006D4A56` (길이 `96` bytes)
- VA: `0x00000001406D49F6`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BB110`
- 디코드: `27`개 명령, `96/96` bytes 표시
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
006D49F6  40 55                           push rbp
006D49F8  48 83 EC 30                     sub rsp, 0x30
006D49FC  48 8B EA                        mov rbp, rdx
006D49FF  88 4D 50                        mov byte ptr [rbp + 0x50], cl
006D4A02  84 C9                           test cl, cl
006D4A04  74 49                           je 0x1406d4a4f
006D4A06  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D4A09  83 F8 07                        cmp eax, 7
006D4A0C  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D4A0F  75 38                           jne 0x1406d4a49
006D4A11  83 C0 07                        add eax, 7
006D4A14  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D4A17  48 8D 85 98 01 00 00            lea rax, [rbp + 0x198]
006D4A1E  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
006D4A25  48 83 A5 C0 00 00 00 00         and qword ptr [rbp + 0xc0], 0
006D4A2D  48 8B 8D 98 01 00 00            mov rcx, qword ptr [rbp + 0x198]
006D4A34  48 89 8D C0 00 00 00            mov qword ptr [rbp + 0xc0], rcx
006D4A3B  48 8B 85 80 01 00 00            mov rax, qword ptr [rbp + 0x180]
006D4A42  48 D3 C8                        ror rax, cl
006D4A45  8B 00                           mov eax, dword ptr [rax]
006D4A47  EB 06                           jmp 0x1406d4a4f
006D4A49  83 C0 0A                        add eax, 0xa
006D4A4C  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D4A4F  48 83 C4 30                     add rsp, 0x30
006D4A53  5D                              pop rbp
006D4A54  C3                              ret
006D4A55  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTimeRefreshDpcRoutine_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int8 *)(a2 + 80) = a1;
    if (a1 == 0) goto loc_006D4A4F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) != 7) goto loc_006D4A49;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 48))) + (7));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
    *(unsigned __int64 *)(a2 + 184) = a2 + 408;
    *(unsigned __int64 *)(a2 + 192) = *(unsigned __int64 *)(a2 + 408);
    goto loc_006D4A4F;
loc_006D4A49:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 384)))) + (10));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
loc_006D4A4F:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpTimeRefreshDpcRoutine_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    *(uint8_t *)(arg2 + 0x50) = Arg1;
    if (Arg1 == 0) goto loc_006D4A4F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) != 7) goto loc_006D4A49;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x30))) + (7));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
    *(void **)(arg2 + 0xB8) = Arg2 + 408;
    *(uint64_t *)(arg2 + 0xC0) = *(uint64_t *)(arg2 + 0x198);
    goto loc_006D4A4F;
loc_006D4A49:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x180)))) + (10));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
loc_006D4A4F:
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
| `Arg2` | `+ 0x50` | `8` | `W` |
| `Arg2` | `+ 0xB8` | `64` | `W` |
| `Arg2` | `+ 0xC0` | `64` | `R/W` |
| `Arg2` | `+ 0xC0` | `64` | `W` |
| `Arg2` | `+ 0x180` | `64` | `R` |
| `Arg2` | `+ 0x198` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D49F6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D49F6[BB_006D49F6]
  bb_006D4A06[BB_006D4A06]
  bb_006D4A11[BB_006D4A11]
  bb_006D4A49[BB_006D4A49]
  bb_006D4A4F[BB_006D4A4F]
  bb_006D4A55[BB_006D4A55]
  bb_006D49F6 -->|branch| bb_006D4A4F
  bb_006D49F6 -->|fallthrough| bb_006D4A06
  bb_006D4A06 -->|branch| bb_006D4A49
  bb_006D4A06 -->|fallthrough| bb_006D4A11
  bb_006D4A11 -->|branch| bb_006D4A4F
  bb_006D4A49 -->|flow| bb_006D4A4F
```
