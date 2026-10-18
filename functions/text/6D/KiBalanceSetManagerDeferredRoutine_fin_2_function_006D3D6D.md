# KiBalanceSetManagerDeferredRoutine$fin$2

- RVA: `0x006D3D6D`–`0x006D3DCB` (길이 `94` bytes)
- VA: `0x00000001406D3D6D`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B35D4`
- 디코드: `26`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006D3D9C` → [local_unwind](../4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006D3D8E` → RVA `0x00494FA5` (`.text`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D3D6D  40 55                           push rbp
006D3D6F  48 83 EC 30                     sub rsp, 0x30
006D3D73  48 8B EA                        mov rbp, rdx
006D3D76  88 4D 49                        mov byte ptr [rbp + 0x49], cl
006D3D79  84 C9                           test cl, cl
006D3D7B  74 47                           je 0x1406d3dc4
006D3D7D  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D3D80  83 F8 28                        cmp eax, 0x28
006D3D83  75 1D                           jne 0x1406d3da2
006D3D85  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D3D88  83 C0 0A                        add eax, 0xa
006D3D8B  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D3D8E  48 8D 15 10 12 DC FF            lea rdx, [rip - 0x23edf0]
006D3D95  48 8B 8D 40 01 00 00            mov rcx, qword ptr [rbp + 0x140]
006D3D9C  E8 9F BD E2 FF                  call 0x1404ffb40
006D3DA1  90                              nop
006D3DA2  48 83 A5 88 00 00 00 00         and qword ptr [rbp + 0x88], 0
006D3DAA  48 8B 8D E7 00 00 00            mov rcx, qword ptr [rbp + 0xe7]
006D3DB1  48 89 8D 88 00 00 00            mov qword ptr [rbp + 0x88], rcx
006D3DB8  48 8B 85 C7 00 00 00            mov rax, qword ptr [rbp + 0xc7]
006D3DBF  48 D3 C8                        ror rax, cl
006D3DC2  8B 00                           mov eax, dword ptr [rax]
006D3DC4  48 83 C4 30                     add rsp, 0x30
006D3DC8  5D                              pop rbp
006D3DC9  C3                              ret
006D3DCA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiBalanceSetManagerDeferredRoutine_fin_2(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int8 *)(a2 + 73) = a1;
    if (a1 == 0) goto loc_006D3DC4;
    result = (unsigned int)(*(unsigned int *)(a2 + 48));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) == 40) {
        result = *(unsigned int *)(a2 + 48);
        result = (unsigned int)((result) + (10));
        *(unsigned int *)(a2 + 48) = (unsigned int)(result);
        a2 = v_rip - 2354672;
        a1 = *(unsigned __int64 *)(a2 + 320);
        result = local_unwind(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(a2 + 136) = *(unsigned __int64 *)(a2 + 231);
loc_006D3DC4:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 199)));
}
```

## 5. (Beta) C Style

```c
int64_t KiBalanceSetManagerDeferredRoutine_fin_2(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    *(uint8_t *)(arg2 + 0x49) = Arg1;
    if (Arg1 == 0) goto loc_006D3DC4;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x30));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) == 40) {
        result = *(uint32_t *)(arg2 + 0x30);
        result = (uint32_t)((result) + (10));
        *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
        Arg2 = v_rip - 2354672;
        Arg1 = *(uint64_t *)(arg2 + 0x140);
        result = local_unwind(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(arg2 + 0x88) = *(uint64_t *)(arg2 + 0xE7);
loc_006D3DC4:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xC7)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x49` | `8` | `W` |
| `Arg2` | `+ 0x88` | `64` | `R/W` |
| `Arg2` | `+ 0x88` | `64` | `W` |
| `Arg2` | `+ 0xC7` | `64` | `R` |
| `Arg2` | `+ 0xE7` | `64` | `R` |
| `Arg2` | `+ 0x140` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D3D6D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D3D6D[BB_006D3D6D]
  bb_006D3D7D[BB_006D3D7D]
  bb_006D3D85[BB_006D3D85]
  bb_006D3DA2[BB_006D3DA2]
  bb_006D3DC4[BB_006D3DC4]
  bb_006D3DCA[BB_006D3DCA]
  bb_006D3D6D -->|branch| bb_006D3DC4
  bb_006D3D6D -->|fallthrough| bb_006D3D7D
  bb_006D3D7D -->|branch| bb_006D3DA2
  bb_006D3D7D -->|fallthrough| bb_006D3D85
  bb_006D3D85 -->|flow| bb_006D3DA2
  bb_006D3DA2 -->|flow| bb_006D3DC4
```
