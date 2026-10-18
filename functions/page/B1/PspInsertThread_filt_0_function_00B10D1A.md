# PspInsertThread$filt$0

- RVA: `0x00B10D1A`–`0x00B10D44` (길이 `42` bytes)
- VA: `0x0000000140B10D1A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A5D9C`
- 디코드: `14`개 명령, `42/42` bytes 표시
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
00B10D1A  40 55                           push rbp
00B10D1C  48 83 EC 40                     sub rsp, 0x40
00B10D20  48 8B EA                        mov rbp, rdx
00B10D23  48 89 8D 90 00 00 00            mov qword ptr [rbp + 0x90], rcx
00B10D2A  48 8B 01                        mov rax, qword ptr [rcx]
00B10D2D  8B 08                           mov ecx, dword ptr [rax]
00B10D2F  89 4D 70                        mov dword ptr [rbp + 0x70], ecx
00B10D32  33 C0                           xor eax, eax
00B10D34  81 F9 4A 00 00 C0               cmp ecx, 0xc000004a
00B10D3A  0F 94 C0                        sete al
00B10D3D  48 83 C4 40                     add rsp, 0x40
00B10D41  5D                              pop rbp
00B10D42  C3                              ret
00B10D43  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspInsertThread_filt_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(a2 + 144) = a1;
    *(unsigned int *)(a2 + 112) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))));
    result = 0;
    result = (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))) == 0xC000004AULL) ? 1 : 0;
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspInsertThread_filt_0(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    *(void **)(arg2 + 0x90) = Arg1;
    *(uint32_t *)(arg2 + 0x70) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))));
    result = 0;
    result = (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))) == 0xC000004AULL) ? 1 : 0;
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x70` | `32` | `W` |
| `Arg2` | `+ 0x90` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B10D1A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B10D1A[BB_00B10D1A]
  bb_00B10D43[BB_00B10D43]
```
